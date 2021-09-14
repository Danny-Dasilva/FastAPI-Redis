import aioredis
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
import uvicorn
from app.utils.cache import FastAPICache
from app.utils.redis.redis import RedisBackend
from app.utils.redis_decorator import cache

app = FastAPI()


@cache()
async def get_cache():
    return 1


@app.get("/")
@cache(expire=60)
async def index(request: Request, response: Response):
    return dict(hello="world")


@app.on_event("startup")
async def startup():
    redis =  aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, debug=True, workers=2,  use_colors=True)