from typing import Optional

from pydantic import BaseModel

class MemoDTO(BaseModel):
    tempindex: Optional[int]
    id: Optional[str]
    index: Optional[int]
    content: Optional[str]
    title: Optional[str]
    class Config:
        orm_mode = True

