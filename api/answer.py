import json
class ApiException(Exception):
    pass

class ApiAnswer:
    def __init__(self, status: bool, response: ..., error: ApiException | None):
        self.__status = status
        self.__response = response
        self.__error = error
    def as_dict(self):
        return {
            'status': self.__status,
            'response': self.__response,
            'error': str(self.__error)
        }
    @property
    def status(self):
        return self.__status
    @property
    def response(self):
        return self.__response
    @property
    def err(self):
        return self.__error
    def json(self):
        return json.dumps(
            self.as_dict(),
            ensure_ascii=False,
            indent=4,
            default=str
        )
    @classmethod
    def ok(cls, response: ...):
        return cls(True, response, None)
    @classmethod
    def error(cls, error: ApiException | str):
        if isinstance(error, str):
            error = ApiException(error)
        return cls(False, None, error)
    def __str__(self):
        return self.json()
