# coding:utf-8
import os
import sys
from os.path import join

_cfg = None


class HuobiConfig(object):

    def __init__(self):
        self.BUNDLE_PATH = '/opt/data'
        self.SYMBOLS = ['btcusdt','ethusdt','xrpusdt','bchusdt','eosusdt','ltcusdt','adausdt','trxusdt']
        self.ID = 'id12'
        pass

    def get_symbols(self):
        return self.SYMBOLS
        pass

    def get_id(self):
        return self.ID
        pass

    def get_bcolz_tick_path(self, code):
        p = join(self.BUNDLE_PATH, "bituptick", code)
        if not os.path.exists(p):
            os.makedirs(p)
        return p
        pass


def get_config():
    global _cfg
    if not _cfg:
        _cfg = HuobiConfig()
    return _cfg
