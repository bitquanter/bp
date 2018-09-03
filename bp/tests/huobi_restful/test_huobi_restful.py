# -*- coding: utf-8 -*-
import json
from HuobiServices import *


def get_huobi_symbols():
    strSymbol = get_symbols()
    print( strSymbol)
    strJsonSymbols = json.dumps(strSymbol)
    return strJsonSymbols

def dump_trading_pair():
    a = get_huobi_symbols()
    j = json.loads(a)


if __name__ == '__main__':
	symbols = get_symbols()
	symbols = symbols['data']
	base = ['btc','eth','xrp','bch','eos','ltc','ada','iota','trx','xlm']
	for s in symbols:
		if s['quote-currency'] == 'usdt':
			if s['base-currency'] in base:
				print(s)
	# huobi_coin_pair = {}
	# for s in symbols:
	# 	if s['quote-currency'] not in huobi_coin_pair:
	# 		huobi_coin_pair[s['quote-currency']] = []
	# 	huobi_coin_pair[s['quote-currency']].append(s['base-currency'])
	# for hcp in huobi_coin_pair:
	# 	print(hcp,huobi_coin_pair[hcp])
    
