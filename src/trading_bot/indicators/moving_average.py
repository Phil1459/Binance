import numpy as np
from binance.spot import Spot

from .indicator import Indicator


class MovingAverage(Indicator):
    """
        Moving Average Indicator
    """

    def __init__(
        self,
        binance_client: Spot,
        symbol: str,
        window_size: int,
    ) -> None:
        self.binance_client = binance_client
        self.symbol = symbol
        self.window_size = window_size

    def _get_data(self) -> np.ndarray:
        data = self.binance_client.klines(
            symbol=self.symbol,
            interval="1m",
            limit=10
        )

        return [ float(item[4]) for item in data ]

    def calculate(self) -> float:
        data = self._get_data()

        print(data)

        weights = np.ones(self.window_size) / self.window_size
        sma = np.convolve(data, weights, mode="valid")

        return sma[0]
