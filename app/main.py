import os
import sys
import logging
from fastapi_sqlalchemy import DBSessionMiddleware
from mangum import Mangum

from .database import init_db
from .entities.calendar import Calendar
from .entities.history import History
from .entities.memo import Memo
from .entities.user import User
from .env import DB_URL

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from fastapi import FastAPI, APIRouter

from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader

from .routers.memo import router as memo_router
from .routers.history import router as history_router
from .routers.calendar import router as calendar_router
from .routers.loluuid import router as loluuid_router
from .routers.user import router as user_router
from .routers.explanation import router as explain_router


API_TOKEN = "SECRET_API_TOKEN"
api_key_header = APIKeyHeader(name="Token")

router = APIRouter()
router.include_router(memo_router, prefix="/memo", tags=["memo"])
router.include_router(history_router, prefix="/history", tags=["history"])
router.include_router(user_router, prefix="/user", tags=["user"])
router.include_router(calendar_router, prefix="/calendar", tags=["calendar"])
router.include_router(loluuid_router, prefix="/loluuid", tags=["loluuid"])
router.include_router(explain_router, prefix="/explain2", tags=["explain"])

app = FastAPI()
app.include_router(router)
origins = ["3.35.91.131", "43.201.121.65"] #"43.201.121.65": api,
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.router.redirect_slashes = False
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

handler = Mangum(app)


@app.get("/")
async def get():
    return {"Hi": "this is teamproject!!!!!"}


@app.on_event("startup")
async def on_startup():
    print('******************************************1')
    await init_db()


