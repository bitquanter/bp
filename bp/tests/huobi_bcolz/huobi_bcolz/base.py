# coding:utf-8
import json

huobi_dic = {}
huobi_dic['usdt'] = ['btc', 'eth', 'xrp', 'bch', 'eos', 'ltc', 'trx', 'neo', 'dash', 'xem', 'ven', 'etc', 'qtum', 'zec', 'omg', 'zil', 'gnt', 'iost', 'snt', 'hsr', 'nas', 'elf', 'ela', 'ht']
huobi_dic['btc'] = ['eth', 'xrp', 'bch', 'eos', 'ltc', 'trx', 'neo', 'dash', 'xem', 'ven', 'etc', 'qtum', 'icx', 'zec', 'omg', 'lsk', 'zil', 'btg', 'ont', 'zrx', 'btm', 'bcd', 'gnt', 'iost', 'snt', 'hsr', 'dgd', 'bat', 'nas', 'elf', 'wicc', 'ela', 'gas', 'knc', 'cmt', 'qash', 'ht', 'eng', 'salt']
huobi_dic['eth'] = ['eos', 'trx', 'ven', 'qtum', 'icx', 'omg', 'lsk', 'zil', 'ont', 'btm', 'gnt', 'iost', 'hsr', 'dgd', 'bat', 'nas', 'elf', 'wicc', 'ela', 'gas', 'cmt', 'qash', 'ht', 'eng', 'salt']


def get_trade_symbol():
    res = []
    for k in huobi_dic:
        for i in huobi_dic[k]:
            tradeStr = '%s%s'%(i,k)
            res.append(tradeStr)
    return res
    pass
