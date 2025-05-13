from fastapi import FastAPI
from middleware.request_logger import RequestLoggingMiddleware
from services.tithi_service import TithiService
from services.festival_service import FestivalService
from api.endpoints import create_router

app = FastAPI()

# Add request logging middleware
app.add_middleware(RequestLoggingMiddleware)

# Initialize services
tithi_service = TithiService()
festival_service = FestivalService()

# Create and include router
router = create_router(tithi_service, festival_service)
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
