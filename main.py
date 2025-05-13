from fastapi import FastAPI

from api.endpoints import create_router
from services.festival_service import FestivalService
from services.tithi_service import TithiService

app = FastAPI(title="Prapanchang API", version="1.0.0")

# Initialize services
tithi_service = TithiService()
festival_service = FestivalService()

# Create and include router
router = create_router(tithi_service, festival_service)
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
