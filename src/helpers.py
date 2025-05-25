import pandas as pd
import datetime
import time

def get_utc(timestamp: int) -> datetime:
    adjusted_timestamp = timestamp/1000
    utc = datetime.datetime.fromtimestamp(adjusted_timestamp)
    return utc


def get_currencies(client, symbols: list = None) -> pd.DataFrame:
    if symbols is None:
        symbols = ["BTC", "BNB", "USDT", "ETH", "SOL", "XRP", "APE"] 

    account = client.account()
    balances = account["balances"]
    
    filtered = [entry for entry in balances if entry["asset"] in symbols]

    df = pd.DataFrame(filtered)
    return df

def get_time_offset(client):
    server_time = client.time()["serverTime"]
    local_time = int(time.time() * 1000)
    return server_time - local_time