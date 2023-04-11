from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = "users"
    nickname = Column(String(50))
    tier = Column(String(30))
    win_rate = Column(String(30))
    most = Column(String(30))
    level = Column(Integer)
    password = Column(String(20))
    id = Column(String(50), primary_key=True)

    calendars = relationship('Calendar', back_populates='user')
    memos = relationship('Memo', back_populates='user')
    histories = relationship('History', back_populates='user')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'nickname: {self.nickname}, \n' \
               f'tier: {self.tier}, \n' \
               f'win_rate: {self.win_rate}, \n' \
               f'most: {self.most}, \n' \
               f'level: {self.level}, \n' \
               f'password: {self.password}, \n' \
               f'id: {self.id}, \n' \
