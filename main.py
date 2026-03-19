from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from app.api.routes import router
from app.core.rate_limit import check_rate_limit
import logging
import traceback

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Trade Opportunities API",
    description="Analyzes market data and provides trade opportunity insights for specific sectors in India.",
    version="1.0.0"
)

# Apply global request rate limiter middleware
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    # Allows bypassing checks for /docs or /openapi.json if needed
    if not request.url.path.startswith(("/docs", "/openapi.json")):
        check_rate_limit(request)
    
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        # Catch unexpected errors gracefully
        logger.error(f"Global exception: {str(e)}")
        logger.debug(traceback.format_exc())
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

# Include the main router
app.include_router(router)

# Custom exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"message": "Invalid input provided.", "details": exc.errors()},
    )
