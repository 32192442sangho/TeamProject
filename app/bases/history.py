from abc import ABCMeta, abstractmethod

from app.schemas.history import HistoryDTO


class HistoryBase(metaclass=ABCMeta):

    @abstractmethod
    def get_history(self, request_history: HistoryDTO): pass

    @abstractmethod
    def update_userid(self, request_history: HistoryDTO): pass

    @abstractmethod
    def update_history(self, request_history: HistoryDTO): pass

    @abstractmethod
    def find_user(self, request_history: HistoryDTO): pass

    @abstractmethod
    def df_to_sql_by_userid(self, request_history: HistoryDTO): pass

    @abstractmethod
    def find_userid_by_api(self, request_history: HistoryDTO): pass

    @abstractmethod
    def find_uuid_by_api(self, request_history: HistoryDTO): pass

    @abstractmethod
    def find_uuid_by_api(self, request_history: HistoryDTO): pass