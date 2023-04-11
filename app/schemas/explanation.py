from typing import Optional

from pydantic import BaseModel


class ExplainVo(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class ExplainDTO(ExplainVo):
    videopath: str

    def __str__(self):
        return f'videopath: {self.videopath},' \

