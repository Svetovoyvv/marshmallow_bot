from orm import base, sa

class Client(base):
    __tablename__ = 'client'
    id = sa.Column(sa.Integer, primary_key=True)
    chat_id = sa.Column(sa.Integer, unique=True)
    phone_number = sa.Column(sa.String(20), unique=True)
    reg_date = sa.Column(sa.DateTime, server_default=sa.func.now())

    def as_dict(self):
        return dict(
            id=self.id,
            chat_id=self.chat_id,
            phone_number=self.phone_number,
            reg_date=str(int(self.reg_date.timestamp()))
        )
