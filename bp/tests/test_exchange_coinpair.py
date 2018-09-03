#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


def coin_map_exchange_contraint():
    with open("bpp_coin_exchange_pair.json", "r", encoding="UTF-8") as f:

        coinpair2exchange = json.load(f)
    # 倒转k v
    ex_coin = {}
    for coin_pair in coinpair2exchange:
        if coinpair2exchange[coin_pair] not in ex_coin:
            ex_coin[coinpair2exchange[coin_pair]] = []
        ex_coin[coinpair2exchange[coin_pair]].append(coin_pair)
    for ex in ex_coin:
        print(ex,ex_coin[ex])

coin_map_exchange_contraint()