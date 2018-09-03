# coding:utf-8
from websocket import create_connection
import gzip
import time
import sys
import json
import bcolz
import os
import numpy as np
from config import get_config

cfg = get_config()


def _update_bcolz_data(symbol):
    item = {}
    item['req'] = 'market.%s.detail'%(symbol)
    item['id'] = cfg.get_id()
    tradeStr = json.dumps(item)
    rootdir = cfg.get_bcolz_tick_path(symbol)
    bcolz_exist = os.path.exists(os.path.join(rootdir, "__rootdirs__"))
    while(1):
        try:
            ws = create_connection("wss://api.huobipro.com/ws")
            break
        except:
            print('connect ws error,retry...')
            time.sleep(5)

    ws.send(tradeStr)
    values = []
    if bcolz_exist:
        ct = bcolz.open(rootdir)
    while(1):
        compressData=ws.recv()
        result=gzip.decompress(compressData).decode('utf-8')
        if result[:7] == '{"ping"':
            ts=result[8:21]
            pong='{"pong":'+ts+'}'
            ws.send(pong)
            ws.send(tradeStr)
        else:
            res = json.loads(result)
            data = res['data']
            #print(data)
            v = [res['ts'],data['low'],data['count'],data['close'],data['vol'],data['id'],data['amount'],data['version'],data['high'],data['open']]
            values.append(v)
            if len(values) == 10:
                a = np.array(values).reshape(len(values), 10)
                columns = list(a.T)
                if bcolz_exist:
                    #ct = bcolz.open(rootdir)
                    ct.append(columns)
                    ct.flush()
                else:
                    names = ['ts','low','count','close','vol','id','amount','version','high','open']
                    ba = bcolz.ctable(columns=columns, mode='w', names=names, rootdir=rootdir)
                    ba.flush()
                    bcolz_exist = True
                del values[:]
    pass
