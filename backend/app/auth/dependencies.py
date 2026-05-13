from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.auth.utils import verify_token

from app.database.connection import SessionLocal
from app.database.models import User


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = verify_token(token)

        email = payload.get("sub")

        db: Session = SessionLocal()

        user = db.query(User).filter(
            User.email == email
        ).first()

        if not user:

            raise HTTPException(
                status_code=401,
                detail="Invalid authentication"
            )

        return user

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )