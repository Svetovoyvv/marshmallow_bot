from .answer import ApiAnswer
from imports import *
class shop:
    @staticmethod
    def get_all() -> ApiAnswer:
        t = session.execute(q.select(Shop).where(Shop.active == True)).fetchall()
        return ApiAnswer.ok(t)
    @staticmethod
    def get_products(shop_id: int) -> ApiAnswer:
        t = session.execute(q.select(Product).where(Product.shop_id == shop_id)).fetchall()
        return ApiAnswer.ok(t)
