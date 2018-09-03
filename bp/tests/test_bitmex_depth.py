#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals
from websocket import create_connection
import sys,os
import gzip
import time
import logging
import json



if __name__ == '__main__':
    while(1):
        try:
            ws = create_connection("wss://www.bitmex.com/realtime")
            break
        except:
            print('connect ws error,retry...')
            time.sleep(5)
    item = {}
    item['op'] = 'subscribe'
    item['args'] = ['orderBook10:XBTUSD','orderBook10:BTCUSD']
    sub_str = json.dumps(item)
    ws.send(sub_str)
    while(1):
        result=ws.recv()
        print(result)
        print('===================================')
