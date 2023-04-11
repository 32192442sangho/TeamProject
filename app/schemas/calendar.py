from typing import Optional

from pydantic import BaseModel

class CalendarDTO(BaseModel):
    index: Optional[int]
    date: str
    start: Optional[int]
    end: Optional[int]
    content: Optional[str]
    id: str
    class Config:
        orm_mode = True



