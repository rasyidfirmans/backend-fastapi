import uuid

from fastapi import Depends
from sqlmodel import Session

from src.database.connection import get_session
from src.database.models.user import User


class UserRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get(self, user_id: uuid.UUID) -> User:
        user = self.session.get(User, user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        return user

    def update(self, user_id: uuid.UUID, data: User) -> None:
        user = self.session.get(User, user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        user.sqlmodel_update(user)
        self.session.add(user)
        self.session.commit()

    def delete(self, user_id: uuid.UUID) -> None:
        user = self.session.get(User, user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        self.session.delete(user)
        self.session.commit()
