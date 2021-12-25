from typing import Optional

from fastapi import Depends

from src.app.db.session import get_session, Session
from src.app.models.user import ModelUser


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_by_email(self, *, email: str) -> Optional[ModelUser]:
        return (
            self.session
            .query(ModelUser)
            .filter(ModelUser.email == email)
            .first()
        )

