from abc import abstractmethod, ABCMeta
from typing import List

from app.schemas.user import UserDTO


class UserBase(metaclass=ABCMeta):
    @abstractmethod
    def add_user(self, request_user: UserDTO): pass

    @abstractmethod
    def login_user(self, request_user: UserDTO): pass

    @abstractmethod
    def logout_user(self, request_user: UserDTO): pass

    @abstractmethod
    def delete_user(self, request_user: UserDTO): pass

    @abstractmethod
    def update_user(self, request_user: UserDTO): pass

    @abstractmethod
    def find_user_by_userid(self, request_user: UserDTO): pass

    @abstractmethod
    def find_user_by_id_for_update(self, request_user: UserDTO): pass

    @abstractmethod
    def find_user_by_token(self, request_user: UserDTO): pass

    @abstractmethod
    def find_uuid_by_userid(self, request_user: UserDTO): pass

    @abstractmethod
    def match_token(self, request_user: UserDTO): pass