import logging
from kiteconnect import KiteConnect, KiteTicker
import pandas as pd

kite = ''
tokens = []
logging.basicConfig(filename='ticks.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def print_hi(name):
    global kite, tokens
    print('temp')

    api_key = open('api_key.txt', 'r').read()
    api_secret = open('api_secret.txt', 'r').read()
    kite = KiteConnect(api_key=api_key)


    # access_token = open('access_token.txt', 'r').read()
    # data = kite.generate_session(access_token, api_secret=api_secret)
    # kite.set_access_token(data["access_token"])

    request_token = "BUquM8rxDaFhjJFPA3EA8rSEPx9rEX8B"

    print(kite.login_url())
    print('abc')


    # here
    # data = kite.generate_session(request_token, api_secret=api_secret)
    # print(data['access_token'])
    # kite.set_access_token(data['access_token'])
    #
    # with open('access_token.txt', 'w') as ak:
    #     ak.write(data['access_token'])


    access_token = open('access_token.txt', 'r').read()
    kite.set_access_token(access_token)


    tokens = [12691970]
    print("Tokens length", len(tokens))

    kws = KiteTicker(api_key, access_token)
    print(kws)
    kws.on_tick = on_tick
    kws.on_connect = on_connect
    kws.on_close = on_close
    kws.connect()

    while True:
        #do nothing
        a = 0

    # Place an order
    print(kite.orders())

def place_order():
    try:
        order_id = kite.place_order(tradingsymbol="INFY",
                                    variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=1,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product=kite.PRODUCT_NRML)

        logging.info("Order placed. ID is: {}".format(order_id))
    except Exception as e:
        logging.info("Order placement failed: {}".format(e.message))
    return order_id


# Callback for tick reception.
def on_tick(tick, ws):
    print(tick)
    logging.debug(tick)

# Callback for successful connection.
def on_connect(ws, response):
	ws.subscribe(tokens)
	ws.set_mode(ws.MODE_FULL, tokens)


def on_close(ws, code, reason):
    ws.stop()


if __name__ == '__main__':
    print_hi('PyCharm')

