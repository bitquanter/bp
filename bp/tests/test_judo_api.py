import requests
import json

requests_session = requests.Session()
url = 'http://39.106.217.163:8083'


def test_login():
    param = {}
    param['email'] = ''
    param['password'] = ''
    s = requests_session.post(url + '/api/v1/login', json.dumps(param)).content
    s = json.loads(s)
    print(s)
    pass


def test_order():
    param = {}
    param['exchange'] = 'huobi'
    param['account_id'] = 'huobi1'
    param['symbol'] = 'btc/usdt'
    param['direction'] = 's'
    param['entrust_price'] = 6000
    param['entrust_volume'] = 10
    param['trader_id'] = 'bp10'
    s = requests_session.post(url + '/api/v1/order', json.dumps(param)).content
    #s = json.loads(s)
    print(s)
    pass


def test_cancel():
    param = {}
    param['entrust_id'] = 10
    s = requests_session.post(
        url + '/api/v1/order_cancel', json.dumps(param)).content
    #s = json.loads(s)
    print(s)
    pass


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-t', '--task', default='order')
    options = parser.parse_args()
    if options.task == 'login':
        test_login()
        pass
    elif options.task == 'order':
        test_order()
        pass
    elif options.task == 'cancel':
        test_cancel()
        pass
    else:
        print('wrong task')
        pass
    pass


if __name__ == '__main__':
    main()
