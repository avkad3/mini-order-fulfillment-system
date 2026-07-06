from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
)
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):

    token = AuthService.login(
        db,
        request.username,
        request.password,
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    return TokenResponse(
        access_token=token,
    )