import logging

from .indicators.moving_average import MovingAverage
from .dependencies.binance import get_spot_client


client = get_spot_client()

moving_average = MovingAverage(binance_client=client, symbol="APEUSDT", window_size=10)

print(moving_average.calculate())
