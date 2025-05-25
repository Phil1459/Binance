from pydantic import BaseModel


class BinanceSettings(BaseModel):
    """
    Binance Settings
    """

    api_key: str
    secret_key: str
    base_url: str
