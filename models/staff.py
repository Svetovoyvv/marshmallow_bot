from orm import base, sa, relationship


class Staff(base):
    __tablename__ = 'staff'
    id = sa.Column(sa.Integer, primary_key=True)
    client_id = sa.Column(sa.Integer, sa.ForeignKey('client.id'))
    client = relationship('Client', backref='staff')
    full_name = sa.Column(sa.String(100))
    admin = sa.Column(sa.Boolean, default=False)
    shop_id = sa.Column(sa.Integer, sa.ForeignKey('shop.id'), nullable=False)
    shop = relationship('Shop', backref='staff')
