# coding:utf-8
from websocket import create_connection
import gzip
import time
import sys
import json
import os
from config import get_config

cfg = get_config()


def _update_redis_data(symbol):
    item = {}
    item['req'] = 'market.%s.detail'%(symbol)
    item['id'] = cfg.get_id()
    tradeStr = json.dumps(item)
    while(1):
        try:
            ws = create_connection("wss://api.huobipro.com/ws")
            break
        except:
            print('connect ws error,retry...')
            time.sleep(5)

    ws.send(tradeStr)
    while(1):
        compressData=ws.recv()
        result=gzip.decompress(compressData).decode('utf-8')
        if result[:7] == '{"ping"':
            ts=result[8:21]
            pong='{"pong":'+ts+'}'
            ws.send(pong)
            ws.send(tradeStr)
        else:
            print(result)
    pass
