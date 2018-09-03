import fcoin
import time

api = fcoin.authorize('cc6110ca00234e768cc4436c69e582c2', '78d616712b5b461c99f677dc9629de48')
server_time = api.server_time()
print(server_time)
# now_ms = int(time.time())
# api.market.ping(now_ms)



# fcoin_ws = fcoin.init_ws()
# topics = ["depth.L20.ethbtc", "depth.L100.btcusdt"]
# fcoin_ws.handle(print)
# fcoin_ws.sub(topics)
