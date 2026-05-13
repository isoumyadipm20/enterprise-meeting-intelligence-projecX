from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.auth.schemas import (
    UserCreate,
    UserLogin
)

from app.auth.utils import (
    hash_password,
    verify_password,
    create_access_token
)

from app.database.connection import SessionLocal
from app.database.models import User

router = APIRouter()


@router.post("/signup")
def signup(user: UserCreate):

    db: Session = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(
        user.password
    )

    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User created successfully"
    }


@router.post("/login")
def login(user: UserLogin):

    db: Session = SessionLocal()

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    valid_password = verify_password(
        user.password,
        db_user.password_hash
    )

    if not valid_password:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={
            "sub": db_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

from fastapi import Depends

from app.auth.dependencies import (
    get_current_user
)


@router.get("/me")
def get_me(
    current_user = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }


from fastapi import APIRouter

from app.nlp.summarizer import generate_summary

router = APIRouter()


@router.post("/summarize")
def summarize_meeting(data: dict):

    transcript = data["transcript"]

    summary = generate_summary(transcript)

    return {
        "summary": summary
    }