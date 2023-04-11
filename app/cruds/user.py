from sqlalchemy.orm import Session
from ..entities.user import User
from ..schemas.user import UserDTO, UserUpdate, UserDelete
from ..services.user_history.user import ApiUser


class UserCrud:
    def __init__(self, db: Session):
        self.db = db

    def signup_user(self, request_user: UserDTO):
        user = User(**request_user.dict())
        self.db.add(user)
        self.db.commit()
        return "Success"

    def search_by_id(self, request_user: UserDTO):
        user = self.db.query(User).filter(User.id == request_user.id, User.password == request_user.password).first()
        return user

    def search_by_id_for_nickname(self, userid):
        user = self.db.query(User).filter(User.id == userid).first()
        return user

    def id_exists(self, request_user: UserDTO):
        user = self.db.query(User).filter(User.id == request_user.id).first()
        return bool(user)

    def password_exists(self, password: str):
        user = self.db.query(User).filter(User.password == password).first()
        return bool(user)

    def update_password(self, user_id: str, request_user: UserUpdate):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
        except:
            return "No Such User"
        if user.password == request_user.old_password:
            user.password = request_user.new_password
            self.db.commit()
            return "Password changed successfully"
        else:
            return "Incorrect old password"

    def delete_user(self, user_id: str, request_user: UserDelete):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
        except:
            return "No Such User"
        if user.password == request_user.password:
            self.db.delete(user)
            self.db.commit()
            return "Account deleted successfully"
        else:
            return "Incorrect password"

    def update_nickname(self, user_id: str, nickname: str) -> None:
        user = self.db.query(User).filter_by(id=user_id).first()
        if user:
            user.nickname = nickname
            self.db.commit()

    def update_else(self, user_id: str, nickname: str):
        update_target = self.db.query(User).filter_by(id=user_id).first()
        info = ApiUser().user_info(nickname)
        update_target.tier = info["tier"]
        update_target.win_rate = info["win_rate"]
        update_target.most = info["most"]
        update_target.level = info["level"]

