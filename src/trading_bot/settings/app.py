from pydantic_settings import BaseSettings, SettingsConfigDict

from .binance import BinanceSettings


class Settings(BaseSettings):
    """
    Settings for Trading Bot
    """

    binance: BinanceSettings

    model_config = SettingsConfigDict(
        env_nested_delimiter="_", env_nested_max_split=1, env_file=".env"
    )
