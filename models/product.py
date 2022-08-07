from orm import base, sa, relationship


class Product(base):
    __tablename__ = 'product'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(256))
    description = sa.Column(sa.Text)
    image = sa.Column(sa.String(256))
    price = sa.Column(sa.Integer)
    shop_id = sa.Column(sa.ForeignKey('shop.id'), default=1)
    shop = relationship('Shop', backref='products')
