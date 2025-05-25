from binance.spot import Spot

from ..settings.app import Settings


settings = Settings()


def get_spot_client() -> Spot:
    """
    Returns: Spot
    """
    client = Spot(
        api_key=settings.binance.api_key,
        api_secret=settings.binance.secret_key,
        base_url=settings.binance.base_url,
    )

    return client
