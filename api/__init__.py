from .client import client as api_client
from .shop import shop as api_shop
from .order import order as api_order
class api:
    client = api_client
    shop = api_shop
    order = api_order

