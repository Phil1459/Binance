from verification import api_keys_testnet as bkt
from binance.spot import Spot
from src import helpers


def main():
    client = Spot(bkt.api_key, bkt.secret_key,base_url='https://testnet.binance.vision')
    print("Account balance start: \n",helpers.get_currencies(client))
    print(client.ticker_price(symbol="APEUSDT"))

    # Post a new order
    params = {
        'symbol': 'APEUSDT',
        'side': 'SELL',
        'type': 'MARKET',
        'quantity': 100  
    }
    response = client.new_order(**params)
    print(response)
    print("Account balance end: \n",helpers.get_currencies(client))

if __name__ == "__main__":
    main()