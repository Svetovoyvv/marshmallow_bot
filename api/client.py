from imports import *
from .answer import ApiAnswer
class client:
    @staticmethod
    def get(client_id: int = None,
            chat_id: int = None,
            phone_number: str = None) -> ApiAnswer:
        # print(session)
        args = [
            (Client.id, client_id),
            (Client.chat_id, chat_id),
            (Client.phone_number, phone_number)
        ]
        args = list(filter(lambda a: a[1] is not None, args))
        if len(args) == 0:
            return ApiAnswer.error('Не указан ни один из параметров')

        cl = session.execute(q.select(Client).where(args[0][0] == args[0][1])).fetchone()
        if cl is None:
            return ApiAnswer.ok(None)
        return ApiAnswer.ok(cl[0])
    @staticmethod
    def add(chat_id: int, phone_number: str) -> ApiAnswer:
        cl = session.execute(q.select(Client).where(Client.chat_id == chat_id)).fetchone()
        if cl is not None:
            return ApiAnswer.error('Клиент уже зарегистрирован.')
        session.execute(q.insert(Client).values(chat_id=chat_id, phone_number=phone_number))
        cl = session.execute(q.select(Client).where(Client.chat_id == chat_id)).fetchone()
        session.commit()
        return ApiAnswer.ok(cl[0].id)