import logging

from .dependencies.binance import get_spot_client


client = get_spot_client()

# params = {"omitZeroBalances": "true"}

# Get account information
# print(client.account(**params))

params = {"symbol": "BTCUSDT", "interval": "1m", "limit": 1}

klines = client.klines(**params)

print(klines)
