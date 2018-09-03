# -*- coding: utf-8 -*-
import multiprocessing
from config import get_config
from write_bcolz import _update_bcolz_data
from print_console import _print_to_console
from write_db import _update_db_data
from write_redis import _update_redis_data
from base import get_trade_symbol

cfg = get_config()


if __name__ == '__main__':
    #请求 Market Detail 数据
    symbols = cfg.get_symbols()
    workers = []
    for s in symbols:
        proc = multiprocessing.Process(target=_print_to_console, args=(s,))
        proc.daemon = True
        proc.start()
        workers.append(proc)
    for proc in workers:
            proc.join()



def main(args):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--write', default='redis')
    options = parser.parse_args()

    symbols = cfg.get_symbols()
    if options.write == 'shell':
        func = _print_to_console
    elif options.write == 'db':
        func = _update_db_data
    elif options.write == 'bcolz':
        func = _update_bcolz_data
    elif options.write == 'redis':
        func = _update_redis_data
    else:
        symbols = get_trade_symbol()
        func = _print_to_console
    workers = []
    for s in symbols:
        proc = multiprocessing.Process(target=func, args=(s,))
        proc.daemon = True
        proc.start()
        workers.append(proc)
    for proc in workers:
            proc.join()
    pass


if __name__ == '__main__':
    main(sys.argv[1:])