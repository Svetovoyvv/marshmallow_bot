from orm import base, sa, relationship

class Order(base):
    __tablename__ = 'order'
    id = sa.Column(sa.Integer, primary_key=True)
    client_id = sa.Column(sa.Integer, sa.ForeignKey('client.id'))
    client = relationship('Client', backref='orders')
    shop_id = sa.Column(sa.Integer, sa.ForeignKey('shop.id'), nullable=False)
    shop = relationship('Shop', backref='orders')
    status = sa.Column(sa.Integer, default=1)
    product_id = sa.Column(sa.ForeignKey('product.id'), nullable=False)
    product = relationship('Product', backref='orders')
    count = sa.Column(sa.Integer, nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())

    @property
    def status_text(self):
        return self.statuses[self.status]

    @property
    def statuses(self):
        return {
            1: 'Принят',
            2: 'Готовится',
            3: 'Готов'
        }
