

from fastapi import APIRouter, Depends
from riotwatcher import ApiError
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.cruds.history import HistoryCrud
from app.database import get_db
from app.schemas.history import HistoryDTO

router = APIRouter()


@router.get("/get", status_code=201)
async def get_history(dto: HistoryDTO, db : Session = Depends(get_db)):
    try:
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=HistoryCrud(db).get_history(request_history=dto)))
    except ApiError as e:
        if e.response.status_code == 404:
            return "잘못 된 값입니다"
        else:
            return {"Error": e}
#{"nickname":"hide on bush"}

@router.put("/put", status_code=201)
async def put_history(dto: HistoryDTO, db:Session = Depends(get_db)):
    try:
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=HistoryCrud(db).update_history(request_history=dto)))
    except ApiError as e:
        if e.response.status_code == 404:
            return "잘못 된 값입니다"
        else:
            return {"Error": e}
        #{"nickname": "hide on bush", "id": "1111"}