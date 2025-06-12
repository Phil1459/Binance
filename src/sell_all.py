from verification import api_keys_testnet as bkt
from binance.spot import Spot
from binance.error import ClientError
import pandas as pd
import logging

def get_all_currencies(client, cur: str) -> pd.DataFrame:
    """
    Retrieves all non-zero currency balances from the user's Binance account.

    Parameters:
        client: An authenticated Binance client instance.
        cur (str): The currency symbol to exclude from the results (e.g. "USDT").

    Returns:
        pd.DataFrame: A DataFrame containing only assets with a 'free' balance greater than 0,
                      excluding cur. Columns include 'asset' and 'free'.
    """
    
    account = client.account()
    balances = account["balances"]

    df = pd.DataFrame(balances)
    df["free"] = df["free"].astype(float)
    df = df[df["free"] > 0]
    df = df[df["asset"] != "USDT"]
    df.reset_index(drop=True, inplace=True)
    return df

def sell_all(client, cur: str = "USDT"):
    """
    Sells all non-zero currency balances in the user's Binance account for a specified quote currency.

    Parameters:
        client: An authenticated Binance client instance.
        cur (str, optional): The quote currency to sell into (default is "USDT").
    """

    df = get_all_currencies(client, cur)
    for row in df.itertuples(index=False):
        params = {
            'symbol': row.asset + cur,
            'side': 'SELL',
            'type': 'MARKET',
            'quantity': row.free
        }
        logging.info(f"Attempting to sell: {params}")

        try:
            response = client.new_order(**params)
            logging.info(f"Sell order successful: {response}")

        except ClientError as e:
            logging.error(f"ClientError while selling {params['symbol']}: {e}")
        
        except Exception as e:
            logging.error(f"Unexpected error while selling {params['symbol']}: {e}")

if __name__ == "__main__":
    client = Spot(bkt.api_key, bkt.secret_key,base_url='https://testnet.binance.vision')
    sell_all(client)