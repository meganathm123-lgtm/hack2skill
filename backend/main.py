"""
CrisisConnect AI Backend Entry Point
Run with: uvicorn main:app --host 0.0.0.0 --port 8000
"""
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from loguru import logger
from starlette.responses import JSONResponse
from starlette.status import HTTP_429_TOO_MANY_REQUESTS
from middleware.rate_limiter import rate_limiter
from routes import emergency, auth
from core.config import settings

app = FastAPI(title="CrisisConnect AI Backend", docs_url="/docs")

# CORS (allow all for hackathon)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate Limiting
app.state.limiter = rate_limiter
app.add_exception_handler(HTTP_429_TOO_MANY_REQUESTS, _rate_limit_exceeded_handler)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(emergency.router, prefix="/emergency", tags=["Emergency"])

# Logging
logger.add("logs/backend.log", rotation="1 MB")

# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
