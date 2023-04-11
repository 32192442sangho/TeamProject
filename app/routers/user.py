from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.database import get_db
from app.cruds.user import UserCrud
from app.entities.history import History
from app.schemas.history import HistoryDTO
from app.schemas.user import UserDTO, UserUpdate, UserDelete, NicknameUpdate
from app.schemas.memo import MemoDTO
from app.schemas.calendar import CalendarDTO
from app.entities.memo import Memo
from app.entities.calendar import Calendar
from riotwatcher import ApiError

from app.services.user_history.user import ApiUser

router = APIRouter()

@router.post("/signup")
async def signup_user(dto: UserDTO, db: Session = Depends(get_db)):
    try:
        user_crud = UserCrud(db)
        if user_crud.id_exists(request_user=dto):
            return JSONResponse(status_code=200, content={"message": "ID already exists"})
        return JSONResponse(status_code=200, content={"message": user_crud.signup_user(request_user=dto)})
    except ApiError as e:
        if e.response.status_code == 404:
            return JSONResponse(status_code=400, content={"message": "wrong value"})
        else:
            return JSONResponse(status_code=400, content={"Error": e})


@router.post("/login")
async def login(dto: UserDTO, db: Session = Depends(get_db)):
    try:
        user_crud = UserCrud(db)
        user = user_crud.search_by_id(request_user=dto)
        if not user:
            return JSONResponse(status_code=400, content={"message": "No such user"})
        user_dict = {
            'nickname': user.nickname,
            'tier': user.tier,
            'win_rate': user.win_rate,
            'most': user.most,
            'level': user.level,
            'password': user.password,
            'id': user.id,
        }
        # Check if user has a nickname
        if user.nickname is None:
            print("Nickname is None")
        else:
            ApiUser().user_info(nickname=user.nickname)

        # Query memo, calendar, and history tables for user
        memos = db.query(Memo).filter_by(id=user.id).all()
        calendars = db.query(Calendar).filter_by(id=user.id).all()
        histories = db.query(History).filter_by(id=user.id).all()

        # Convert memo, calendar, and history data to DTOs
        memo_dtos = [MemoDTO.from_orm(memo) for memo in memos]
        calendar_dtos = [CalendarDTO.from_orm(calendar) for calendar in calendars]
        history_dtos = [HistoryDTO.from_orm(history) for history in histories]

        # Create a response dictionary with user, memo, calendar, and history data
        response_data = {"user": user_dict, "memos": memo_dtos, "calendars": calendar_dtos,
                         "histories": history_dtos}

        # Return response as JSON
        return JSONResponse(status_code=200, content=response_data)

    except ApiError as e:
        if e.response.status_code == 404:
            return JSONResponse(status_code=400, content={"message": "wrong value"})
        else:
            return JSONResponse(status_code=400, content={"Error": e})


@router.put("/change_password/{user_id}")
async def change_password(user_id: str, user_update: dict, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    if user_crud.update_password(user_id, UserUpdate(**user_update)):
        return JSONResponse(status_code=200, content={"message": "Password changed successfully"})
    else:
        return JSONResponse(status_code=400, content={"message": "Failed to change password"})
#{old_password:"1111",new_password:"1111"}

@router.delete("/delete_account/{user_id}")
async def delete_account(user_id: str, user_delete: dict, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    if user_crud.delete_user(user_id, UserDelete(**user_delete)):
        return JSONResponse(status_code=200, content={"message": "Account deleted successfully"})
    else:
        return JSONResponse(status_code=400, content={"message": "Failed to delete account"})

#{"password":1111}
@router.put("/update_nickname/{user_id}")
async def update_nickname(user_id: str, data: dict, db: Session = Depends(get_db)):
    try:
        # Create UserUpdate model from JSON data
        update_data = NicknameUpdate(**data)

        # Update user nickname in database
        user_crud = UserCrud(db)
        user_crud.update_nickname(user_id, update_data.new_nickname)
        user_crud.update_else(user_id, update_data.new_nickname)
        # Retrieve updated user data from database
        updated_user = user_crud.search_by_id_for_nickname(user_id)
        user_dict = {
            'nickname': updated_user.nickname,
            'tier': updated_user.tier,
            'win_rate': updated_user.win_rate,
            'most': updated_user.most,
            'level': updated_user.level,
            'password': updated_user.password,
            'id': updated_user.id,
        }
        # Retrieve history data for the updated user
        histories = db.query(History).filter_by(id=user_id).all()
        history_dtos = [HistoryDTO.from_orm(history) for history in histories]

        # Create a response dictionary with user and history data
        response_data = {"user": user_dict, "histories": [history.to_dict() for history in history_dtos]}

        # Return updated user and history data as JSON
        return JSONResponse(status_code=200, content=response_data)

    except Exception as e:
        # Return error message as JSON
        return JSONResponse(status_code=400, content={"message": str(e)})\
#{new_nickname:"32131"}