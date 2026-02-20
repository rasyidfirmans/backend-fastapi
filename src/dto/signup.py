from pydantic import BaseModel

from src.dto.base import Response


class SignupRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
    confirm_password: str


class SignupResponse(Response):
    pass
