# -*- coding: utf-8 -*-
import redis
import sys
import time


def main(args):
    client = redis.StrictRedis.from_url('18.182.50.195:6379')
    while (1):
        #st = client.get('market.btcusdt.depth.step0')
        st = client.get('tick/huobi/btcusdt')
        if st:
            print(st)
        else:
        	print('nul')
        time.sleep(2)
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
