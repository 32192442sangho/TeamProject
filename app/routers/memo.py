from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.database import get_db
from app.entities.memo import Memo
from app.schemas.memo import MemoDTO
from app.cruds.memo import MemoCrud

from app.schemas.memo import MemoDTO

router = APIRouter()


@router.post("/create")
async def create_memo(dto: MemoDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200, content=dict(message=MemoCrud(db).create_memo_CRUD(request_memo=dto)))
#{"id":"1111","index":1,"content":"안녕하세요","title":"인사"}

@router.get("/read/{id}/{index}")
async def read_memo(index: int, id: str, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200, content=dict(message=MemoCrud(db).read_memo_CRUD(index=index, uuid=id)))
#주소만

@router.delete("/delete/{id}/{index}")
async def create_memo(index: int, id: str, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200, content=dict(message=MemoCrud(db).delete_memo_CRUD(index=index, id=id)))
#주소만