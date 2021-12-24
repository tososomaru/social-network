from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_session
from ..models.users import UserCreate, UserUpdate
from ..tables import User


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id) -> User:
        user = (
            self.session
            .query(User)
            .filter_by(id=user_id)
            .first()
        )
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user

    def get_users(self) -> List[User]:
        return self.session.query(User).all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._get(user_id)

    def create_user(self, user_data) -> UserCreate:
        user = User(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        return user

    def update_user(self, user_id: int, user_data: UserUpdate):
        user = self._get(user_id)
        for k, v in user_data:
            setattr(user, k, v)
        self.session.commit()
        return user

    def delete_user(self, user_id: int) -> None:
        user = self._get(user_id)
        self.session.delete(user)
        self.session.commit()
