from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class History(Base):
    __tablename__ = "history"

    history = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(30), ForeignKey('users.id'), nullable=False)
    nickname = Column(String(50))
    matchid = Column(String(30), nullable=False)
    uuid = Column(String(500))
    champion = Column(String(30))
    result = Column(String(30))
    kills = Column(String(30))
    deaths = Column(String(30))
    assists = Column(String(30))
    kda = Column(String(30))
    position = Column(String(30))
    minute = Column(Integer, nullable=False)
    candle = Column(Integer, nullable=False)

    user = relationship('User', back_populates='histories')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'넘버: {self.history}, \n ' \
               f'이름: {self.id}, \n ' \
               f'uuid: {self.uuid}, \n' \
               f'matchid: {self.matchid}, \n' \
               f'result: {self.result}, \n' \
               f'kills: {self.kills} \n' \
               f'deaths: {self.deaths} \n' \
               f'assists: {self.assists} \n' \
               f'kda: {self.kda} \n' \
               f'position: {self.position} \n'
