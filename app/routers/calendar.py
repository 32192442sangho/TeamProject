from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.cruds.calendar import CalendarCrud
from app.database import get_db
from app.entities.memo import Memo
from app.schemas.calendar import CalendarDTO
from app.schemas.memo import MemoDTO
from app.cruds.memo import MemoCrud

from app.schemas.memo import MemoDTO

router = APIRouter()


@router.post("/create")
async def create_calendar(dto: CalendarDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200, content=dict(message=CalendarCrud(db).create_calendar_CRUD(request_calendar=dto)))
#{"date": "dsadsaa","start": 1,"end": 2,"content": "dsadsad","id": "1111"}

@router.get("/read/{id}/{date}")
async def read_calendar(date: str, id: str, db: Session = Depends(get_db)):
    calendar = CalendarCrud(db).read_calendar_CRUD(date=date, id=id)
    calendar_json = [{'index':c.index,'id': c.id, 'date': str(c.date), 'start': c.start, 'end': c.end, 'content': c.content} for c in calendar]
    print(calendar_json)
    return JSONResponse(status_code=200, content={"data": calendar_json})
#주소만

@router.delete("/delete")
async def create_calendar(dto: CalendarDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200, content=dict(message=CalendarCrud(db).delete_calendar_CRUD(dto)))
#{"index": 1,"date": "2020-12-12","id": "1111"}