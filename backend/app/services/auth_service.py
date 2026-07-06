from sqlalchemy.orm import Session

from app.core.security import (
    verify_password,
    create_access_token,
)

from app.repositories.user_repository import UserRepository


class AuthService:

    @staticmethod
    def login(
        db: Session,
        username: str,
        password: str,
    ):

        user = UserRepository.get_by_username(
            db,
            username,
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.password_hash,
        ):
            return None

        token = create_access_token(
            {
                "sub": user.username,
                "role": user.role.value,
            }
        )

        return token