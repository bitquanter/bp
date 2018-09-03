# -*- coding:utf-8 -*-
from depth_api import  tk_parse
import gevent
from gevent import monkey
monkey.patch_all()

class Depth(object):
    def __init__(self):
        self.fcoin = ['fcoin/btc.usdt', 'fcoin/eth.usdt', 'fcoin/xrp.usdt', 'fcoin/bch.usdt', 'fcoin/ltc.usdt',
                      'fcoin/etc.usdt', 'fcoin/but.eth']
        self.binance_list = ['binance/btc.usdt', 'binance/eth.usdt', 'binance/bcc.usdt', 'binance/ltc.usdt',
                             'binance/neo.usdt', 'binance/bnb.usdt', 'binance/qtum.usdt', 'binance/eth.btc',
                             'binance/xrp.btc', 'binance/bcc.btc', 'binance/eos.btc', 'binance/ltc.btc',
                             'binance/ada.btc', 'binance/xlm.btc', 'binance/trx.btc', 'binance/neo.btc',
                             'binance/xmr.btc', 'binance/dash.btc', 'binance/ven.btc', 'binance/etc.btc',
                             'binance/bnb.btc', 'binance/qtum.btc', 'binance/icx.btc', 'binance/zec.btc',
                             'binance/omg.btc', 'binance/lsk.btc', 'binance/zil.btc', 'binance/btg.btc',
                             'binance/ae.btc', 'binance/ont.btc', 'binance/xvg.btc', 'binance/steem.btc',
                             'binance/zrx.btc', 'binance/nano.btc', 'binance/bts.btc', 'binance/ppt.btc',
                             'binance/bcd.btc', 'binance/waves.btc', 'binance/strat.btc', 'binance/iost.btc',
                             'binance/snt.btc', 'binance/wtc.btc', 'binance/hsr.btc', 'binance/dgd.btc',
                             'binance/aion.btc', 'binance/lrc.btc', 'binance/bat.btc', 'binance/kmd.btc',
                             'binance/elf.btc', 'binance/ark.btc', 'binance/pivx.btc', 'binance/bnt.btc',
                             'binance/gas.btc', 'binance/knc.btc', 'binance/fun.btc', 'binance/gxs.btc',
                             'binance/cmt.btc', 'binance/sub.btc', 'binance/storm.btc', 'binance/xzc.btc',
                             'binance/eng.btc', 'binance/nuls.btc', 'binance/salt.btc', 'binance/gto.btc',
                             'binance/xrp.eth', 'binance/bcc.eth', 'binance/eos.eth', 'binance/ltc.eth',
                             'binance/ada.eth', 'binance/xlm.eth', 'binance/trx.eth', 'binance/neo.eth',
                             'binance/xmr.eth', 'binance/dash.eth', 'binance/ven.eth', 'binance/etc.eth',
                             'binance/bnb.eth', 'binance/qtum.eth', 'binance/icx.eth', 'binance/zec.eth',
                             'binance/omg.eth', 'binance/lsk.eth', 'binance/zil.eth', 'binance/btg.eth',
                             'binance/ae.eth', 'binance/ont.eth', 'binance/xvg.eth', 'binance/steem.eth',
                             'binance/zrx.eth', 'binance/nano.eth', 'binance/bts.eth', 'binance/ppt.eth',
                             'binance/bcd.eth', 'binance/waves.eth', 'binance/strat.eth', 'binance/iost.eth',
                             'binance/snt.eth', 'binance/wtc.eth', 'binance/hsr.eth', 'binance/dgd.eth',
                             'binance/aion.eth', 'binance/lrc.eth', 'binance/bat.eth', 'binance/kmd.eth',
                             'binance/elf.eth', 'binance/ark.eth', 'binance/pivx.eth', 'binance/bnt.eth',
                             'binance/knc.eth', 'binance/fun.eth', 'binance/gxs.eth', 'binance/cmt.eth',
                             'binance/sub.eth', 'binance/storm.eth', 'binance/xzc.eth', 'binance/eng.eth',
                             'binance/nuls.eth', 'binance/salt.eth', 'binance/gto.eth']
        self.huobi_list = ['huobip/btc.usdt', 'huobip/eth.usdt', 'huobip/xrp.usdt', 'huobip/bch.usdt',
                           'huobip/eos.usdt', 'huobip/ltc.usdt', 'huobip/trx.usdt', 'huobip/neo.usdt',
                           'huobip/dash.usdt', 'huobip/xem.usdt', 'huobip/ven.usdt', 'huobip/etc.usdt',
                           'huobip/qtum.usdt', 'huobip/zec.usdt', 'huobip/omg.usdt', 'huobip/zil.usdt',
                           'huobip/gnt.usdt', 'huobip/iost.usdt', 'huobip/snt.usdt', 'huobip/hsr.usdt',
                           'huobip/nas.usdt', 'huobip/elf.usdt', 'huobip/ela.usdt', 'huobip/ht.usdt', 'huobip/eth.btc',
                           'huobip/xrp.btc', 'huobip/bch.btc', 'huobip/eos.btc', 'huobip/ltc.btc', 'huobip/trx.btc',
                           'huobip/neo.btc', 'huobip/dash.btc', 'huobip/xem.btc', 'huobip/ven.btc', 'huobip/etc.btc',
                           'huobip/qtum.btc', 'huobip/icx.btc', 'huobip/zec.btc', 'huobip/omg.btc', 'huobip/lsk.btc',
                           'huobip/zil.btc', 'huobip/btg.btc', 'huobip/ont.btc', 'huobip/zrx.btc', 'huobip/btm.btc',
                           'huobip/bcd.btc', 'huobip/gnt.btc', 'huobip/iost.btc', 'huobip/snt.btc', 'huobip/hsr.btc',
                           'huobip/dgd.btc', 'huobip/bat.btc', 'huobip/nas.btc', 'huobip/elf.btc', 'huobip/wicc.btc',
                           'huobip/ela.btc', 'huobip/gas.btc', 'huobip/knc.btc', 'huobip/cmt.btc', 'huobip/qash.btc',
                           'huobip/ht.btc', 'huobip/eng.btc', 'huobip/salt.btc', 'huobip/eos.eth', 'huobip/trx.eth',
                           'huobip/ven.eth', 'huobip/qtum.eth', 'huobip/icx.eth', 'huobip/omg.eth', 'huobip/lsk.eth',
                           'huobip/zil.eth', 'huobip/ont.eth', 'huobip/btm.eth', 'huobip/gnt.eth', 'huobip/iost.eth',
                           'huobip/hsr.eth', 'huobip/dgd.eth', 'huobip/bat.eth', 'huobip/nas.eth', 'huobip/elf.eth',
                           'huobip/wicc.eth', 'huobip/ela.eth', 'huobip/gas.eth', 'huobip/cmt.eth', 'huobip/qash.eth',
                           'huobip/ht.eth', 'huobip/eng.eth', 'huobip/salt.eth']
        self.bittfinex_list = ['bitfinex/btc.usd', 'bitfinex/eth.usd', 'bitfinex/xrp.usd', 'bitfinex/bch.usd',
                               'bitfinex/eos.usd', 'bitfinex/ltc.usd', 'bitfinex/xlm.usd', 'bitfinex/trx.usd',
                               'bitfinex/neo.usd', 'bitfinex/xmr.usd', 'bitfinex/ven.usd', 'bitfinex/etc.usd',
                               'bitfinex/zec.usd', 'bitfinex/omg.usd', 'bitfinex/btg.usd', 'bitfinex/xvg.usd',
                               'bitfinex/zrx.usd', 'bitfinex/rep.usd', 'bitfinex/mkr.usd', 'bitfinex/gnt.usd',
                               'bitfinex/snt.usd', 'bitfinex/lrc.usd', 'bitfinex/bat.usd', 'bitfinex/elf.usd',
                               'bitfinex/knc.usd', 'bitfinex/fun.usd', 'bitfinex/eth.btc', 'bitfinex/xrp.btc',
                               'bitfinex/bch.btc', 'bitfinex/eos.btc', 'bitfinex/ltc.btc', 'bitfinex/xlm.btc',
                               'bitfinex/trx.btc', 'bitfinex/neo.btc', 'bitfinex/xmr.btc', 'bitfinex/ven.btc',
                               'bitfinex/etc.btc', 'bitfinex/zec.btc', 'bitfinex/omg.btc', 'bitfinex/btg.btc',
                               'bitfinex/xvg.btc', 'bitfinex/zrx.btc', 'bitfinex/rep.btc', 'bitfinex/mkr.btc',
                               'bitfinex/gnt.btc', 'bitfinex/snt.btc', 'bitfinex/lrc.btc', 'bitfinex/bat.btc',
                               'bitfinex/elf.btc', 'bitfinex/knc.btc', 'bitfinex/fun.btc', 'bitfinex/bch.eth',
                               'bitfinex/eos.eth', 'bitfinex/xlm.eth', 'bitfinex/trx.eth', 'bitfinex/neo.eth',
                               'bitfinex/ven.eth', 'bitfinex/omg.eth', 'bitfinex/xvg.eth', 'bitfinex/zrx.eth',
                               'bitfinex/rep.eth', 'bitfinex/mkr.eth', 'bitfinex/gnt.eth', 'bitfinex/snt.eth',
                               'bitfinex/lrc.eth', 'bitfinex/bat.eth', 'bitfinex/elf.eth', 'bitfinex/knc.eth',
                               'bitfinex/fun.eth']
        self.bittrex_list = ['bittrex/btc.usdt', 'bittrex/eth.usdt', 'bittrex/xrp.usdt', 'bittrex/bcc.usdt',
                             'bittrex/ltc.usdt', 'bittrex/ada.usdt', 'bittrex/trx.usdt', 'bittrex/neo.usdt',
                             'bittrex/xmr.usdt', 'bittrex/dash.usdt', 'bittrex/etc.usdt', 'bittrex/zec.usdt',
                             'bittrex/omg.usdt', 'bittrex/btg.usdt', 'bittrex/xvg.usdt', 'bittrex/sc.usdt',
                             'bittrex/nxt.usdt', 'bittrex/eth.btc', 'bittrex/xrp.btc', 'bittrex/bcc.btc',
                             'bittrex/ltc.btc', 'bittrex/ada.btc', 'bittrex/xlm.btc', 'bittrex/trx.btc',
                             'bittrex/neo.btc', 'bittrex/xmr.btc', 'bittrex/dash.btc', 'bittrex/xem.btc',
                             'bittrex/etc.btc', 'bittrex/qtum.btc', 'bittrex/zec.btc', 'bittrex/omg.btc',
                             'bittrex/lsk.btc', 'bittrex/btg.btc', 'bittrex/dcr.btc', 'bittrex/xvg.btc',
                             'bittrex/steem.btc', 'bittrex/zrx.btc', 'bittrex/sc.btc', 'bittrex/waves.btc',
                             'bittrex/strat.btc', 'bittrex/rep.btc', 'bittrex/doge.btc', 'bittrex/gnt.btc',
                             'bittrex/dgb.btc', 'bittrex/snt.btc', 'bittrex/lrc.btc', 'bittrex/bat.btc',
                             'bittrex/kmd.btc', 'bittrex/ark.btc', 'bittrex/ardr.btc', 'bittrex/pivx.btc',
                             'bittrex/poly.btc', 'bittrex/bnt.btc', 'bittrex/sys.btc', 'bittrex/rdd.btc',
                             'bittrex/mona.btc', 'bittrex/storm.btc', 'bittrex/fct.btc', 'bittrex/xzc.btc',
                             'bittrex/eng.btc', 'bittrex/nxt.btc', 'bittrex/salt.btc', 'bittrex/xrp.eth',
                             'bittrex/bcc.eth', 'bittrex/ltc.eth', 'bittrex/ada.eth', 'bittrex/xlm.eth',
                             'bittrex/trx.eth', 'bittrex/neo.eth', 'bittrex/xmr.eth', 'bittrex/dash.eth',
                             'bittrex/xem.eth', 'bittrex/etc.eth', 'bittrex/qtum.eth', 'bittrex/zec.eth',
                             'bittrex/omg.eth', 'bittrex/btg.eth', 'bittrex/zrx.eth', 'bittrex/sc.eth',
                             'bittrex/waves.eth', 'bittrex/strat.eth', 'bittrex/rep.eth', 'bittrex/gnt.eth',
                             'bittrex/dgb.eth', 'bittrex/snt.eth', 'bittrex/lrc.eth', 'bittrex/bat.eth',
                             'bittrex/poly.eth', 'bittrex/bnt.eth', 'bittrex/storm.eth', 'bittrex/fct.eth',
                             'bittrex/eng.eth', 'bittrex/salt.eth']
        self.bitz_list = ['bitz/eth.btc', 'bitz/bch.btc', 'bitz/eos.btc', 'bitz/ltc.btc', 'bitz/trx.btc',
                          'bitz/dash.btc', 'bitz/etc.btc', 'bitz/qtum.btc', 'bitz/zec.btc', 'bitz/omg.btc',
                          'bitz/lsk.btc', 'bitz/btg.btc', 'bitz/bcd.btc', 'bitz/doge.btc', 'bitz/dgb.btc',
                          'bitz/hsr.btc', 'bitz/ark.btc', 'bitz/gxs.btc', 'bitz/fct.btc', 'bitz/nuls.btc',
                          'bitz/trx.eth', 'bitz/doge.eth', 'bitz/gxs.eth', 'bitz/nuls.eth']
        self.gdax_list = ['gdax/btc.usd', 'gdax/eth.usd', 'gdax/bch.usd', 'gdax/ltc.usd', 'gdax/eth.btc',
                          'gdax/bch.btc', 'gdax/ltc.btc']
        self.hitbit_list = ['hitbit/btc.usd', 'hitbit/eth.usd', 'hitbit/xrp.usd', 'hitbit/bch.usd', 'hitbit/eos.usd',
                            'hitbit/ltc.usd', 'hitbit/ada.usd', 'hitbit/xlm.usd', 'hitbit/trx.usd', 'hitbit/neo.usd',
                            'hitbit/xmr.usd', 'hitbit/dash.usd', 'hitbit/xem.usd', 'hitbit/ven.usd', 'hitbit/etc.usd',
                            'hitbit/bcn.usd', 'hitbit/qtum.usd', 'hitbit/icx.usd', 'hitbit/zec.usd', 'hitbit/omg.usd',
                            'hitbit/lsk.usd', 'hitbit/btg.usd', 'hitbit/ont.usd', 'hitbit/xvg.usd', 'hitbit/zrx.usd',
                            'hitbit/nano.usd', 'hitbit/btm.usd', 'hitbit/strat.usd', 'hitbit/rep.usd',
                            'hitbit/doge.usd', 'hitbit/gnt.usd', 'hitbit/dgb.usd', 'hitbit/snt.usd', 'hitbit/kmd.usd',
                            'hitbit/ardr.usd', 'hitbit/dcn.usd', 'hitbit/bnt.usd', 'hitbit/fun.usd', 'hitbit/mith.usd',
                            'hitbit/sub.usd', 'hitbit/veri.usd', 'hitbit/maid.usd', 'hitbit/nxt.usd', 'hitbit/eth.btc',
                            'hitbit/xrp.btc', 'hitbit/bch.btc', 'hitbit/eos.btc', 'hitbit/ltc.btc', 'hitbit/ada.btc',
                            'hitbit/xlm.btc', 'hitbit/trx.btc', 'hitbit/neo.btc', 'hitbit/xmr.btc', 'hitbit/dash.btc',
                            'hitbit/xem.btc', 'hitbit/ven.btc', 'hitbit/etc.btc', 'hitbit/bcn.btc', 'hitbit/qtum.btc',
                            'hitbit/icx.btc', 'hitbit/zec.btc', 'hitbit/omg.btc', 'hitbit/lsk.btc', 'hitbit/btg.btc',
                            'hitbit/ae.btc', 'hitbit/ont.btc', 'hitbit/xvg.btc', 'hitbit/steem.btc', 'hitbit/zrx.btc',
                            'hitbit/nano.btc', 'hitbit/btm.btc', 'hitbit/sc.btc', 'hitbit/ppt.btc', 'hitbit/waves.btc',
                            'hitbit/strat.btc', 'hitbit/rep.btc', 'hitbit/doge.btc', 'hitbit/gnt.btc',
                            'hitbit/btcp.btc', 'hitbit/dgb.btc', 'hitbit/snt.btc', 'hitbit/wtc.btc', 'hitbit/hsr.btc',
                            'hitbit/dgd.btc', 'hitbit/lrc.btc', 'hitbit/kmd.btc', 'hitbit/ardr.btc', 'hitbit/dcn.btc',
                            'hitbit/bnt.btc', 'hitbit/cnx.btc', 'hitbit/fun.btc', 'hitbit/mith.btc', 'hitbit/sub.btc',
                            'hitbit/storm.btc', 'hitbit/veri.btc', 'hitbit/maid.btc', 'hitbit/nxt.btc',
                            'hitbit/xrp.eth', 'hitbit/bch.eth', 'hitbit/eos.eth', 'hitbit/ltc.eth', 'hitbit/ada.eth',
                            'hitbit/xlm.eth', 'hitbit/trx.eth', 'hitbit/neo.eth', 'hitbit/xmr.eth', 'hitbit/dash.eth',
                            'hitbit/xem.eth', 'hitbit/ven.eth', 'hitbit/etc.eth', 'hitbit/bcn.eth', 'hitbit/qtum.eth',
                            'hitbit/icx.eth', 'hitbit/zec.eth', 'hitbit/omg.eth', 'hitbit/lsk.eth', 'hitbit/btg.eth',
                            'hitbit/ont.eth', 'hitbit/xvg.eth', 'hitbit/zrx.eth', 'hitbit/nano.eth', 'hitbit/btm.eth',
                            'hitbit/ppt.eth', 'hitbit/strat.eth', 'hitbit/rep.eth', 'hitbit/doge.eth', 'hitbit/gnt.eth',
                            'hitbit/dgb.eth', 'hitbit/snt.eth', 'hitbit/lrc.eth', 'hitbit/kmd.eth', 'hitbit/dcn.eth',
                            'hitbit/bnt.eth', 'hitbit/fun.eth', 'hitbit/mith.eth', 'hitbit/sub.eth', 'hitbit/kin.eth',
                            'hitbit/veri.eth', 'hitbit/maid.eth', 'hitbit/eng.eth', 'hitbit/nxt.eth']
        self.kraken_list = ['kraken/eth.usd', 'kraken/xrp.usd', 'kraken/bch.usd', 'kraken/eos.usd', 'kraken/ltc.usd',
                            'kraken/xlm.usd', 'kraken/xmr.usd', 'kraken/dash.usd', 'kraken/usdt.usd', 'kraken/etc.usd',
                            'kraken/zec.usd', 'kraken/rep.usd', 'kraken/eos.eth', 'kraken/etc.eth', 'kraken/rep.eth']
        self.lbank_list = ['lbank/btc.usdt', 'lbank/eth.usdt', 'lbank/bch.usdt', 'lbank/neo.usdt', 'lbank/qtum.usdt',
                           'lbank/zec.usdt', 'lbank/eth.btc', 'lbank/bch.btc', 'lbank/ltc.btc', 'lbank/neo.btc',
                           'lbank/dash.btc', 'lbank/etc.btc', 'lbank/qtum.btc', 'lbank/zec.btc', 'lbank/btg.btc',
                           'lbank/sc.btc', 'lbank/bts.btc', 'lbank/bcd.btc', 'lbank/cmt.btc', 'lbank/bch.eth',
                           'lbank/eos.eth', 'lbank/trx.eth', 'lbank/qtum.eth', 'lbank/zec.eth', 'lbank/btm.eth',
                           'lbank/bts.eth', 'lbank/nas.eth', 'lbank/mith.eth', 'lbank/cmt.eth']
        self.okex_list = ['okex/btc.usdt', 'okex/eth.usdt', 'okex/xrp.usdt', 'okex/bch.usdt', 'okex/eos.usdt',
                          'okex/ltc.usdt', 'okex/xlm.usdt', 'okex/trx.usdt', 'okex/neo.usdt', 'okex/xmr.usdt',
                          'okex/dash.usdt', 'okex/xem.usdt', 'okex/etc.usdt', 'okex/qtum.usdt', 'okex/icx.usdt',
                          'okex/zec.usdt', 'okex/omg.usdt', 'okex/btg.usdt', 'okex/ont.usdt', 'okex/zrx.usdt',
                          'okex/nano.usdt', 'okex/btm.usdt', 'okex/ppt.usdt', 'okex/bcd.usdt', 'okex/mkr.usdt',
                          'okex/gnt.usdt', 'okex/dgb.usdt', 'okex/iost.usdt', 'okex/snt.usdt', 'okex/wtc.usdt',
                          'okex/hsr.usdt', 'okex/dgd.usdt', 'okex/lrc.usdt', 'okex/nas.usdt', 'okex/elf.usdt',
                          'okex/ark.usdt', 'okex/bnt.usdt', 'okex/gas.usdt', 'okex/knc.usdt', 'okex/fun.usdt',
                          'okex/mith.usdt', 'okex/cmt.usdt', 'okex/sub.usdt', 'okex/hot.usdt', 'okex/eng.usdt',
                          'okex/nuls.usdt', 'okex/salt.usdt', 'okex/gto.usdt', 'okex/eth.btc', 'okex/xrp.btc',
                          'okex/bch.btc', 'okex/eos.btc', 'okex/ltc.btc', 'okex/xlm.btc', 'okex/trx.btc',
                          'okex/neo.btc', 'okex/xmr.btc', 'okex/dash.btc', 'okex/xem.btc', 'okex/etc.btc',
                          'okex/qtum.btc', 'okex/icx.btc', 'okex/zec.btc', 'okex/omg.btc', 'okex/btg.btc',
                          'okex/ont.btc', 'okex/zrx.btc', 'okex/nano.btc', 'okex/btm.btc', 'okex/ppt.btc',
                          'okex/bcd.btc', 'okex/mkr.btc', 'okex/gnt.btc', 'okex/dgb.btc', 'okex/iost.btc',
                          'okex/snt.btc', 'okex/wtc.btc', 'okex/hsr.btc', 'okex/dgd.btc', 'okex/lrc.btc',
                          'okex/nas.btc', 'okex/elf.btc', 'okex/ark.btc', 'okex/bnt.btc', 'okex/gas.btc',
                          'okex/knc.btc', 'okex/fun.btc', 'okex/mith.btc', 'okex/cmt.btc', 'okex/sub.btc',
                          'okex/hot.btc', 'okex/eng.btc', 'okex/nuls.btc', 'okex/salt.btc', 'okex/gto.btc',
                          'okex/xrp.eth', 'okex/bch.eth', 'okex/eos.eth', 'okex/ltc.eth', 'okex/xlm.eth',
                          'okex/trx.eth', 'okex/neo.eth', 'okex/xmr.eth', 'okex/dash.eth', 'okex/xem.eth',
                          'okex/etc.eth', 'okex/qtum.eth', 'okex/icx.eth', 'okex/zec.eth', 'okex/omg.eth',
                          'okex/ont.eth', 'okex/zrx.eth', 'okex/nano.eth', 'okex/btm.eth', 'okex/ppt.eth',
                          'okex/mkr.eth', 'okex/gnt.eth', 'okex/dgb.eth', 'okex/iost.eth', 'okex/snt.eth',
                          'okex/wtc.eth', 'okex/hsr.eth', 'okex/dgd.eth', 'okex/lrc.eth', 'okex/nas.eth',
                          'okex/elf.eth', 'okex/ark.eth', 'okex/bnt.eth', 'okex/gas.eth', 'okex/knc.eth',
                          'okex/fun.eth', 'okex/mith.eth', 'okex/cmt.eth', 'okex/sub.eth', 'okex/hot.eth',
                          'okex/eng.eth', 'okex/nuls.eth', 'okex/salt.eth', 'okex/gto.eth']
        self.gateio_list = ['gateio/btc.usdt', 'gateio/eth.usdt', 'gateio/xrp.usdt', 'gateio/bch.usdt',
                            'gateio/eos.usdt', 'gateio/ltc.usdt', 'gateio/ada.usdt', 'gateio/xlm.usdt',
                            'gateio/trx.usdt', 'gateio/neo.usdt', 'gateio/xmr.usdt', 'gateio/dash.usdt',
                            'gateio/ven.usdt', 'gateio/etc.usdt', 'gateio/qtum.usdt', 'gateio/icx.usdt',
                            'gateio/zec.usdt', 'gateio/omg.usdt', 'gateio/lsk.usdt', 'gateio/zil.usdt',
                            'gateio/btg.usdt', 'gateio/ae.usdt', 'gateio/ont.usdt', 'gateio/xvg.usdt',
                            'gateio/zrx.usdt', 'gateio/nano.usdt', 'gateio/btm.usdt', 'gateio/bts.usdt',
                            'gateio/bcd.usdt', 'gateio/waves.usdt', 'gateio/mkr.usdt', 'gateio/doge.usdt',
                            'gateio/gnt.usdt', 'gateio/snt.usdt', 'gateio/hsr.usdt', 'gateio/dgd.usdt',
                            'gateio/lrc.usdt', 'gateio/bat.usdt', 'gateio/nas.usdt', 'gateio/elf.usdt',
                            'gateio/gas.usdt', 'gateio/knc.usdt', 'gateio/fun.usdt', 'gateio/mith.usdt',
                            'gateio/gxs.usdt', 'gateio/qash.usdt', 'gateio/drgn.usdt', 'gateio/salt.usdt',
                            'gateio/eth.btc', 'gateio/xrp.btc', 'gateio/bch.btc', 'gateio/eos.btc', 'gateio/ltc.btc',
                            'gateio/ada.btc', 'gateio/xlm.btc', 'gateio/neo.btc', 'gateio/xmr.btc', 'gateio/dash.btc',
                            'gateio/etc.btc', 'gateio/qtum.btc', 'gateio/zec.btc', 'gateio/omg.btc', 'gateio/lsk.btc',
                            'gateio/btg.btc', 'gateio/ae.btc', 'gateio/xvg.btc', 'gateio/zrx.btc', 'gateio/nano.btc',
                            'gateio/btm.btc', 'gateio/bts.btc', 'gateio/bcd.btc', 'gateio/waves.btc', 'gateio/doge.btc',
                            'gateio/snt.btc', 'gateio/hsr.btc', 'gateio/lrc.btc', 'gateio/bat.btc', 'gateio/nas.btc',
                            'gateio/gas.btc', 'gateio/gxs.btc', 'gateio/qash.btc', 'gateio/eos.eth', 'gateio/xlm.eth',
                            'gateio/trx.eth', 'gateio/ven.eth', 'gateio/etc.eth', 'gateio/qtum.eth', 'gateio/icx.eth',
                            'gateio/omg.eth', 'gateio/zil.eth', 'gateio/ae.eth', 'gateio/ont.eth', 'gateio/zrx.eth',
                            'gateio/btm.eth', 'gateio/rep.eth', 'gateio/mkr.eth', 'gateio/gnt.eth', 'gateio/snt.eth',
                            'gateio/hsr.eth', 'gateio/dgd.eth', 'gateio/lrc.eth', 'gateio/bat.eth', 'gateio/nas.eth',
                            'gateio/elf.eth', 'gateio/bnt.eth', 'gateio/knc.eth', 'gateio/fun.eth', 'gateio/mith.eth',
                            'gateio/qash.eth', 'gateio/drgn.eth', 'gateio/salt.eth']
    def data_parse(self,currency_list):
        tk_parse(currency_list, )

    def fcoin_func(self):
        self.data_parse(self.fcoin)

    def binance_func(self):
        self.data_parse(self.binance_list)

    def huobi_func(self):
        self.data_parse(self.huobi_list)

    def bittfinex_func(self):
        self.data_parse(self.bittfinex_list)

    def bittrex_func(self):
        self.data_parse(self.bittrex_list)

    def bitz_func(self):
        self.data_parse(self.bitz_list)

    def gdax_func(self):
        self.data_parse(self.gdax_list)

    def hitbit_func(self):
        self.data_parse(self.hitbit_list)

    def kraken_func(self):
        self.data_parse(self.kraken_list)

    def lbank_func(self):
        self.data_parse(self.lbank_list)

    def okex_func(self):
        self.data_parse(self.okex_list)

    def gateio_func(self):
        self.data_parse(self.gateio_list)

if __name__ == '__main__':
    obj = Depth()
    g0 = gevent.spawn(obj.fcoin_func)
    g1 = gevent.spawn(obj.binance_func)
    g2 = gevent.spawn(obj.huobi_func)
    g3 = gevent.spawn(obj.bittfinex_func)
    g4 = gevent.spawn(obj.bitz_func)
    g5 = gevent.spawn(obj.gdax_func)
    g6 = gevent.spawn(obj.hitbit_func)
    g7 = gevent.spawn(obj.kraken_func)
    g8 = gevent.spawn(obj.lbank_func)
    g9 = gevent.spawn(obj.okex_func)
    g10 = gevent.spawn(obj.gateio_func)
    g11 = gevent.spawn(obj.binance_func)
    g0.join()
    g1.join()
    g2.join()
    g3.join()
    g4.join()
    g5.join()
    g6.join()
    g7.join()
    g8.join()
    g9.join()
    g10.join()
    g11.join()
