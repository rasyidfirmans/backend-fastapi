from fastapi import APIRouter, Depends

from src.controllers.auth import AuthController
from src.dto.signup import SignupRequest, SignupResponse

router = APIRouter(prefix="/auth")


@router.post("/signup")
def signup(
    req_body: SignupRequest, controller: AuthController = Depends(AuthController)
) -> SignupResponse:
    return controller.signup(req_body)


# @router.post("/login")

# @router.post("/logout")

# @router.post("/me")

# @router.post("/reset-password")
