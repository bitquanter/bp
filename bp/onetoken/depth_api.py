# -*- coding:utf-8 -*-
import json
import time
from websocket import create_connection
from data_save import data_write, write_redis

#实时tike数据接口
def tk_parse(currency_list):
    while True:
        try:
            ws = create_connection("wss://1token.trade/api/v1/ws/tick")
            auth_data = {"uri": "auth"}
            ws.send(json.dumps(auth_data))
            for cur in currency_list:
                request_data = {"uri": "subscribe-single-tick-verbose",
                                "contract": cur}
                ws.send(json.dumps(request_data))
        except:
            time.sleep(0.5)
        else:
            while True:
                try:
                    data = ws.recv()
                except:
                    break
                else:
                    try:
                        json_data = json.loads(data)
                        currency = json_data['data']['contract']
                    except:
                        pass
                    else:
                        key = 'tick/%s'%(currency)
                        value = json.dumps(json_data['data'])
                        write_redis(key, value)
