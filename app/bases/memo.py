from abc import ABCMeta, abstractmethod

from app.schemas.memo import MemoDTO


class MemoBase(metaclass=ABCMeta):

    @abstractmethod
    def create_memo_CRUD(self, request_history: MemoDTO): pass

    @abstractmethod
    def read_memo_CRUD(self, index: int, uuid: str): pass

    @abstractmethod
    def update_memo_CRUD(self, request_history: MemoDTO): pass

    @abstractmethod
    def delete_memo_CRUD(self, index: int, uuid: str): pass


