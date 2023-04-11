from abc import ABCMeta, abstractmethod

from app.schemas.calendar import CalendarDTO


class CalendarBase(metaclass=ABCMeta):
    @abstractmethod
    def create_calendar_CRUD(self, request_calendar: CalendarDTO): pass

    @abstractmethod
    def read_calendar_CRUD(self, date: int, uuid: str): pass

    @abstractmethod
    def delete_calendar_CRUD(self, request_calendar: CalendarDTO): pass
