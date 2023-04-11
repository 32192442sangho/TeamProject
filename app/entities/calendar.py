from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, String, Integer, text, TIMESTAMP, ForeignKey


class Calendar(Base):

    __tablename__ = "calendar"

    index = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(TIMESTAMP, nullable=False)  #timestamp
    start = Column(Integer, nullable=True) #int
    end = Column(Integer, nullable=True) #int
    content = Column(String(100), nullable=False)
    id = Column(String(100), ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='calendars')

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def __str__(self):
        return f'index: {self.index}, \n ' \
               f'date: {self.date}, \n ' \
               f'start: {self.start}, \n' \
               f'end: {self.end}, \n' \
               f'context: {self.content}, \n ' \
                f'uuid : {self.uuid}, \n'