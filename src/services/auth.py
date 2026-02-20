from fastapi import Depends

from src.database.models.user import User
from src.dto.signup import SignupResponse
from src.repositories.user import UserRepository


class AuthService:
    def __init__(self, user_repository: UserRepository = Depends(UserRepository)):
        self.user_repository = user_repository

    def signup(self, user: User) -> SignupResponse:
        user = self.user_repository.create(user)
        return SignupResponse(
            status="success", message="User created successfully", data={"id": user.id}
        )
