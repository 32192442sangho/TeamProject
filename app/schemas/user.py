from typing import Optional

from pydantic import BaseModel


class UserVo(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class UserDTO(UserVo):
    nickname: Optional[str]
    tier: Optional[str]
    win_rate: Optional[str]
    most: Optional[str]
    level: Optional[int]
    password: str
    id: str

    def __str__(self):
        return f'nickname: {self.nickname},' \
               f'tier: {self.tier},' \
               f'win_rate: {self.win_rate},' \
               f'most: {self.most},' \
               f'level: {self.level},' \
               f'password: {self.password}' \
               f'id: {self.id}'



class UserUpdate(BaseModel):
    old_password: str
    new_password: str


class UserDelete(BaseModel):
    password: str


class NicknameUpdate(BaseModel):
    new_nickname: str
