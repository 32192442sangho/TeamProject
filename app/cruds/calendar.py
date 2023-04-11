import json
from abc import ABC
from typing import List

import pymysql
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.bases.calendar import CalendarBase
from app.entities.calendar import Calendar
from app.entities.memo import Memo
from app.schemas.calendar import CalendarDTO

pymysql.install_as_MySQLdb()


class CalendarCrud(CalendarBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def create_calendar_CRUD(self, request_calendar: CalendarDTO):
        db = self.db
        calendar = Calendar(**request_calendar.dict())
        db.add(calendar)
        db.commit()
        db.refresh(calendar)
        return "CREATE_SUCCESS"

    def read_calendar_CRUD(self, date: str, id: str):
        db = self.db
        calendar = db.query(Calendar).filter_by(date=date, id=id).order_by(Calendar.date.asc()).all()
        if not calendar:
            raise HTTPException(status_code=404, detail="CALENDAR_NOT_FOUND")
        return calendar

    def delete_calendar_CRUD(self, request_calendar: CalendarDTO):
        db_calendar = self.db.query(Calendar).filter_by(index=request_calendar.index, id=request_calendar.id, date=request_calendar.date).first()
        if not db_calendar:
            raise HTTPException(status_code=404, detail="MEMO_NOT_FOUND")
        self.db.delete(db_calendar)
        self.db.commit()
        return "DELETE_SUCCESS"