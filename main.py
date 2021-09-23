import aioredis
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
import uvicorn
from app.utils.cache import FastAPICache
from app.utils.redis.redis import RedisBackend
from app.utils.redis_decorator import cache
from app.routes import router as common_routes
app = FastAPI()


app.include_router(common_routes)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, debug=True, workers=2,  use_colors=True)