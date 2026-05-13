from fastapi import FastAPI
from app.reports.routes import router as report_router
from app.database.connection import engine
from app.database.models import Base
from app.nlp.routes import router as nlp_router
from app.auth.routes import router as auth_router
from app.reports.routes import router as report_router
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    nlp_router,
    prefix="/ai",
    tags=["AI NLP"]
)

app.include_router(
    report_router,
    prefix="/reports",
    tags=["Reports"]
)

@app.get("/")
def root():

    return {
        "message": "Meeting Intelligence API Running"
    }

from fastapi import FastAPI

from app.database.connection import engine
from app.database.models import Base

from app.auth.routes import router as auth_router
from app.nlp.routes import router as nlp_router


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    nlp_router,
    prefix="/ai",
    tags=["AI NLP"]
)

app.include_router(
    report_router,
    prefix="/reports",
    tags=["Reports"]
)


@app.get("/")
def root():

    return {
        "message": "Meeting Intelligence API Running"
    }