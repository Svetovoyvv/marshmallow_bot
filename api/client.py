from imports import *
class client:
    @staticmethod
    def get(client_id: int = None,
            chat_id: int = None,
            phone_number: str = None) -> Client:
        args = [
            (Client.id, client_id),
            (Client.chat_id, chat_id),
            (Client.phone_number, phone_number)
        ]
        args = list(filter(lambda a: a[1] is not None, args))
        if len(args) == 0:
            raise ValueError()

        cl = session.execute(q.select(Client).where(args[0][0] == args[0][1])).fetchone()
        if cl is None:
            return ApiAnswer.error('Клиент не найден.')
        return ApiAnswer.ok(cl)
