from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, String, Integer, text, TIMESTAMP, ForeignKey


class Memo(Base):

    __tablename__ = "memo"

    tempindex = Column(Integer, primary_key=True, autoincrement=True) #string
    id = Column(String(100), ForeignKey('users.id'), nullable=False)
    nickname = Column(String(1000))
    index = Column(Integer, nullable=False)
    content = Column(String(5000), nullable=True)
    title = Column(String(50), nullable=True)
    user = relationship('User', back_populates='memos')
    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'tempindex: {self.tempindex}, \n ' \
               f'uuid: {self.uuid}, \n ' \
               f'index: {self.index}, \n' \
               f'content: {self.content}, \n'\
            f'title: {self.title}, \n'

