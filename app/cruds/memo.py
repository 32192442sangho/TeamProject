from abc import ABC
from typing import List

import pymysql
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.bases.memo import MemoBase
from app.entities.memo import Memo
from app.schemas.memo import MemoDTO

pymysql.install_as_MySQLdb()


class MemoCrud(MemoBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def create_memo_CRUD(self, request_memo: MemoDTO):
        db = self.db
        memo = Memo(**request_memo.dict())
        db.add(memo)
        db.commit()
        db.refresh(memo)
        return "CREATE_SUCCESS"

    def read_memo_CRUD(self, index: int, uuid: str):
        db = self.db
        memo = db.query(Memo).filter_by(index=index, id=uuid).first()
        if not memo:
            raise HTTPException(status_code=404, detail="MEMO_NOT_FOUND")
        memo_dic = {
            "tempindex":memo.tempindex,
            "id": memo.id,
            "index": memo.index,
            "content": memo.content,
            "title": memo.title
        }
        return memo_dic

    def update_memo_CRUD(self, request_memo: MemoDTO):
        db = self.db
        new_memo = Memo(**request_memo.dict())
        db_memo = db.query(Memo).filter_by(index=new_memo.index, id=new_memo.id).first()
        if not db_memo:
            return "MEMO_NOT_FOUND"
        db_memo.content = new_memo.content
        db.commit()
        return "UPDATE_SUCCESS"

    def delete_memo_CRUD(self, index, id: str):
        db_memo = self.db.query(Memo).filter_by(index=index, id=id).first()
        if not db_memo:
            raise HTTPException(status_code=404, detail="MEMO_NOT_FOUND")
        self.db.delete(db_memo)
        self.db.commit()
        return "DELETE_SUCCESS"

