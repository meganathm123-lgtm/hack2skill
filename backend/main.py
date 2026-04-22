"""
CrisisConnect AI Backend Entry Point
Run with: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
"""

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from loguru import logger
from starlette.responses import JSONResponse

# Internal imports
from middleware.rate_limiter import rate_limiter
from routes import emergency, auth
from core.config import settings


# =========================
# APP INITIALIZATION
# =========================
app = FastAPI(
    title="CrisisConnect AI Backend",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None
)


# =========================
# MIDDLEWARE
# =========================

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
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# =========================
# ROUTERS
# =========================
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(emergency.router, prefix="/emergency", tags=["Emergency"])


# =========================
# LOGGING
# =========================
logger.add(
    "logs/backend.log",
    rotation="1 MB",
    retention="7 days",
    level="INFO"
)


# =========================
# ROOT HEALTH CHECK
# =========================
@app.get("/")
def root():
    return {
        "message": "CrisisConnect AI Backend Running 🚀",
        "docs": "/docs"
    }


# =========================
# GLOBAL ERROR HANDLER
# =========================
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )