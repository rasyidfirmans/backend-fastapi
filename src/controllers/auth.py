from fastapi import Depends

from src.database.models.user import User
from src.dto.signup import SignupRequest
from src.services.auth import AuthService


class AuthController:
    def __init__(self, auth_service: AuthService = Depends(AuthService)):
        self.auth_service = auth_service

    def signup(self, req_body: SignupRequest):
        user_data = User(
            first_name=req_body.first_name,
            last_name=req_body.last_name,
        )
        response = self.auth_service.signup(user_data)
        return response

    # def login(self):
    #     return auth

    # def logout(self):
    #     return auth

    # def me(self):
    #     return auth

    # def forgot_password(self):
    #     return auth

    # def reset_password(self):
    #     return auth
