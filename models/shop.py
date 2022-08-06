from orm import base, sa


class Shop(base):
    __tablename__ = 'shop'
    id = sa.Column(sa.Integer, primary_key=True)
    address = sa.Column(sa.String(256))
    name = sa.Column(sa.String(256))
    active = sa.Column(sa.Boolean, default=True)


