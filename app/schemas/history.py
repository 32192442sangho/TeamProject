from typing import Optional

from pydantic import BaseModel


class HistoryVo(BaseModel):

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class HistoryDTO(HistoryVo):
    history: Optional[int]
    nickname : Optional[str]
    id: Optional[str]
    uuid: Optional[str]
    matchid = Optional[str]
    champion = Optional[str]
    result = Optional[str]
    kills = Optional[str]
    deaths = Optional[str]
    assists = Optional[str]
    kda = Optional[str]
    position = Optional[str]

    def __str__(self):
        return f'이름: {self.history}, \n ' \
               f'유저 아이디: {self.id} \n ' \
               f'uuid: {self.uuid} \n' \
               f'매치 아이디: {self.matchid} \n' \
               f'결과: {self.result} \n' \
               f'킬 : {self.kills} \n'