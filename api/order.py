from imports import *
from .answer import ApiAnswer
class order:
    @staticmethod
    def add(client_id: int, shop_id: int, product_id: int, count: int) -> ApiAnswer:
        session.add(Order(client_id=client_id, product_id=product_id, count=count, shop_id=shop_id))
        session.commit()
        return ApiAnswer.ok(None)
    @staticmethod
    def get(order_id: int) -> ApiAnswer:
        t = session.execute(q.select(Order).where(Order.id == order_id)).fetchone()
        return ApiAnswer.ok(t[0])
    @staticmethod
    def get_active(client_id: int) -> ApiAnswer:
        t = session.execute(q.select(Order).where(Order.client_id == client_id)).fetchall()
        return ApiAnswer.ok(t)
    @staticmethod
    def get_all(client_id: int) -> ApiAnswer:
        t = session.execute(q.select(Order).where(Order.client_id == client_id)).fetchall()
        return ApiAnswer.ok(t)

