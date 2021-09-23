import aioredis
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
import uvicorn
from app.utils.cache import FastAPICache
from app.utils.redis.redis import RedisBackend
from app.utils.redis_decorator import cache

from fastapi import APIRouter

router = APIRouter()


@cache()
async def get_cache():
    return 1


@router.get("/")
@cache(expire=10)
async def index(request: Request, response: Response):
    from time import sleep
    sleep(3)
    return dict(hello="world")


@router.on_event("startup")
async def startup():
    redis =  aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

