from verification import api_keys_testnet as bkt
from binance.spot import Spot
import datetime

client = Spot(bkt.api_key, bkt.secret_key,base_url='https://testnet.binance.vision')

#Get server time
server_time_unix = client.time()["serverTime"]/1000
server_time_utc = datetime.datetime.fromtimestamp(server_time_unix)
print(server_time_utc)


balance = client.account()
print(balance)

#recend trades
#j = 0
#recent_trades = client.trades("BTCEUR",limit = 100)
#for i in recent_trades:
#    j += 1
#    print(j,i, datetime.datetime.fromtimestamp(i["time"]/1000))