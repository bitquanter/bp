#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals
from websocket import create_connection
from btfxwss import BtfxWss
import sys,os
import gzip
import time
import logging
import json
import requests
from ref.client import Client
from ref.depthcache import DepthCacheManager
from config import get_config
from redis_store import RedisStore

client = Client('', '')

cfg = get_config()
log = logging.getLogger('bpdata')
store = RedisStore()

# _default_refresh = 30 * 60
# def bib_depth_cache_new(self, client, symbol, callback=None, refresh_interval=_default_refresh):
#     self._client = client
#     self._symbol = symbol
#     self._callback = callback
#     self._last_update_id = None
#     self._depth_message_buffer = []
#     self._bm = None
#     self._depth_cache = DepthCache(self._symbol)
#     self._refresh_interval = refresh_interval
#     print(symbol,callback)
#     pass


# DepthCacheManager.__init__ = bib_depth_cache_new


def huobi_depth():
    while True:
        try:
            print('start huobi depth')
            _huobi_depth()
        except:
            print("huobi retry...")


def _huobi_depth():
    # 连接火币行情
    ws = create_connection("wss://api.huobipro.com/ws")
    sym_dic = cfg.get_symbols('huobi')
    symbols = []
    for k in sym_dic:
        for i in sym_dic[k]:
            tradeStr = '%s%s'%(i,k)
            symbols.append(tradeStr)
    print(len(symbols))
    for s in symbols:
        item = {}
        item['sub'] = 'market.%s.depth.step0'%(s)
        item['id'] = cfg.get_id()
        sub_str = json.dumps(item)
        ws.send(sub_str)
    while(1):
        compressData=ws.recv()
        if not isinstance(compressData, bytes):
            print(type(compressData))
            break
        result=gzip.decompress(compressData).decode('utf-8')
        if result[:7] == '{"ping"':
            ts=result[8:21]
            pong='{"pong":'+ts+'}'
            ws.send(pong)
        else:
            res = json.loads(result)
            if 'tick' in res:
                coin_pair = res['ch'].strip().split('.')[1]
                key = 'tick/%s/%s'%('huobi',coin_pair)
                store.set(key, json.dumps(res))
    pass


def okex_depth():
    while True:
        try:
            print('start okex depth')
            _okex_depth()
        except:
            print('okex retry...')
    pass


def _okex_depth():
    # 链接 okex行情
    ws = create_connection("wss://real.okex.com:10441/websocket")
    sym_dic = cfg.get_symbols('okex')
    symbols = []
    for k in sym_dic:
        for i in sym_dic[k]:
            tradeStr = '%s_%s'%(i,k)
            symbols.append(tradeStr)
    print(len(symbols))
    for symbol in symbols:
        item = {}
        item['event'] = 'addChannel'
        item['channel'] = 'ok_sub_spot_%s_depth'%(symbol)
        sub_str = json.dumps(item)
        ws.send(sub_str)
    while(1):
        result=ws.recv()
        res = json.loads(result)[0]
        if 'data' in res and res['channel'] != 'addChannel':
            channel = res['channel'].strip().split('_')
            key = 'tick/%s/%s%s'%('okex',channel[3], channel[4])
            store.set(key, json.dumps(res))
    pass


def binance_depth():
    _binance_depth()
    # while True:
    #     try:
    #         print('start binance depth')
    #         _binance_depth()
    #     except:
    #         print('binance retry...')
    # pass


def _binance_depth():
    # 链接币安行情
    sym_dic = cfg.get_symbols('binance')
    symbols = []
    for k in sym_dic:
        for i in sym_dic[k]:
            tradeStr = '%s%s'%(i,k)
            symbols.append(tradeStr.upper())
    for sym in symbols:
        dcm = DepthCacheManager(client, sym, callback=binance_depth_callback)
    pass


def binance_depth_callback(data):
    if data:
        key = 'tick/%s/%s'%('binance',data.symbol.lower())
        item = {}
        item['ask'] = data.get_asks()[:5] 
        item['bid'] = data.get_bids()[:5]
        item['timestamp'] = time.time()
        print(key)
        store.set(key, json.dumps(item))
    pass


def bitfinex_depth():
    while True:
        try:
            print('start bitfinex depth')
            _bitfinex_depth()
        except:
            print('bitfinex retry...')


def _bitfinex_depth():
    # 连接bitfinex行情
    wss = BtfxWss()
    wss.start()
    while not wss.conn.connected.is_set():
        time.sleep(1)
    sym_dic = cfg.get_symbols('bitfinex')
    symbols = []
    for k in sym_dic:
        for i in sym_dic[k]:
            tradeStr = '%s%s'%(i,k)
            symbols.append(tradeStr.upper())
    print(len(symbols))
    for sym in symbols:
        wss.subscribe_to_order_book(sym)

    while (1):
        for sym in symbols:
            sym_q = wss.books(sym)
            if not sym_q.empty():
                key = 'tick/%s/%s'%('bitfinex', sym.lower())
                data = sym_q.get()
                item = {}
                item['data'] = data[0]
                item['ts'] = data[1]
                store.set(key, json.dumps(item))
    wss.stop()
    pass


def bibox_depth():
    while True:
        try:
            print('start bibox depth')
            _bibox_depth()
        except:
            print('bibox retry...')


def _bibox_depth():
    sym_dic = cfg.get_symbols('bibox')
    symbols = []
    for k in sym_dic:
        for i in sym_dic[k]:
            tradeStr = '%s_%s'%(i, k)
            symbols.append(tradeStr.upper())
    while True:
        for sym in symbols:
            url = 'https://api.bibox.com/v1/mdata?cmd=depth&pair=%s&size=10'%(sym)
            response = requests.request("GET", url)
            #dep = json.loads(response.text)
            key = 'tick/%s/%s'%('bibox',sym.replace('_','').lower())
            store.set(key, response.text)
            time.sleep(0.2)
    pass


def zb_depth():
    while True:
        try:
            print('start zb depth')
            _zb_depth()
        except:
            print('zb retry...')


def _zb_depth():
    # 连接zb行情
    ws = create_connection("wss://api.zb.cn:9999/websocket")
    sym_dic = cfg.get_symbols('zb')
    symbols = []
    for k in sym_dic:
        for i in sym_dic[k]:
            tradeStr = '%s%s'%(i,k)
            symbols.append(tradeStr)
    for s in symbols:
        item = {}
        item['event'] = 'addChannel'
        item['channel'] = '%s_depth'%(s)
        sub_str = json.dumps(item)
        ws.send(sub_str)
    while(1):
        result = ws.recv()
        res_json = json.loads(result)
        key = 'tick/zb/%s'%(res_json['channel'].split('_')[0])
        store.set(key, result)
    pass


def bigone_depth():
    while True:
        try:
            print('start bigone depth')
            _bigone_depth()
        except:
            print('bigone retry...')


def _bigone_depth():
    sym_dic = cfg.get_symbols('bigone')
    symbols = []
    for k in sym_dic:
        for i in sym_dic[k]:
            tradeStr = '%s-%s'%(i, k)
            symbols.append(tradeStr.upper())
    while True:
        for sym in symbols:
            url = 'https://big.one/api/v2/markets/%s/depth'%(sym)
            response = requests.request("GET", url)
            #dep = json.loads(response.text)
            key = 'tick/%s/%s'%('bigone',sym.replace('-','').lower())
            store.set(key, response.text)
            time.sleep(0.01)
    pass


def kucoin_depth():
    while True:
        try:
            print('start kucoin depth')
            _kucoin_depth()
        except:
            print('kucoin retry...')


def _kucoin_depth():
    sym_dic = cfg.get_symbols('kucoin')
    symbols = []
    for k in sym_dic:
        for i in sym_dic[k]:
            tradeStr = '%s-%s'%(i, k)
            symbols.append(tradeStr.upper())
    while True:
        for sym in symbols:
            url = 'https://api.kucoin.com/v1/%s/open/orders'%(sym)
            response = requests.request("GET", url)
            #dep = json.loads(response.text)
            key = 'tick/%s/%s'%('kucoin',sym.replace('-','').lower())
            store.set(key, response.text)
            time.sleep(0.01)
    pass


def fcoin_depth():
    while True:
        try:
            print('start fcoin depth')
            _fcoin_depth()
        except:
            print('fcoin retry...')


def _fcoin_depth():
    # 连接fcoin交易所websocket行情
    # import fcoin
    # fcoin_ws = fcoin.init_ws()
    # sym_dic = cfg.get_symbols('fcoin')
    # topics = []
    # for k in sym_dic:
    #     for i in sym_dic[k]:
    #         tradeStr = 'depth.L20.%s%s'%(i,k)
    #         topics.append(tradeStr)
    # fcoin_ws.handle(fcoin_depth_callback)
    # fcoin_ws.sub(topics)



    # while(1):
    #     try:
    #         ws = create_connection("wss://api.fcoin.com/v2/ws")
    #         break
    #     except:
    #         print('connect ws error,retry...')
    #         time.sleep(5)

    # sym_dic = cfg.get_symbols('fcoin')
    # symbols = []
    # for k in sym_dic:
    #     for i in sym_dic[k]:
    #         tradeStr = '%s%s'%(i,k)
    #         symbols.append(tradeStr)
    # # for symbol in symbols:
    # #     sub_str = 'depth.L20.%s'%(symbol)
    # #     ws.send(sub_str)
    # item = {}
    # item['topic'] = 'depth.L20.%s'%('btcusdt')
    # sub_str = 'depth.L20.%s'%('btcusdt') # json.dumps(item)
    # ws.send(sub_str)
    # while(1):
    #     result=ws.recv()
    #     print(result)
    #     print('=========================')
    pass


def fcoin_depth_callback(data):
    print(data)
    # json_data = json.loads(data)
    # key = 'tick/fcoin/%s'%(json_data['type'].split('.')[2])
    # store.set(key, data)
    pass


def binmex_depth():
    while True:
        try:
            print('start binmex depth')
            _binmex_depth()
        except:
            print('binmex retry...')


def _binmex_depth():
    # 链接 binmex ws
    ws = create_connection("wss://www.bitmex.com/realtime")
    item = {}
    item['op'] = 'subscribe'
    item['args'] = []
    sym_dic = cfg.get_symbols('binmex')
    for k in sym_dic:
        for i in sym_dic[k]:
            tradeStr = 'orderBook10:%s%s'%(i.upper(),k.upper())
            item['args'].append(tradeStr)
    sub_str = json.dumps(item)
    ws.send(sub_str)
    while(1):
        result=ws.recv()
        json_res = json.loads(result)
        if 'data' in json_res and len(json_res['data']) > 0:
            key = 'tick/binmex/%s'%(json_res['data'][0]['symbol'].lower())
            store.set(key, json.dumps(json_res['data'][0]))
    pass


def otcbtc_depth():
    while True:
        try:
            print('start otcbtc depth')
            _otcbtc_depth()
        except:
            print('otcbtc retry...')


def _otcbtc_depth():
    sym_dic = cfg.get_symbols('otcbtc')
    symbols = []
    for k in sym_dic:
        for i in sym_dic[k]:
            tradeStr = '%s%s'%(i, k)
            symbols.append(tradeStr)
    while True:
        for sym in symbols:
            url = 'https://bb.otcbtc.com/api/v2/depth?market=%s&limit=10'%(sym)
            response = requests.request("GET", url)
            #dep = json.loads(response.text)
            key = 'tick/%s/%s'%('otcbtc',sym)
            store.set(key, response.text)
            time.sleep(0.3)
    pass
