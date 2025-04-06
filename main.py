from fastapi import FastAPI
from services.tithi_service import TithiService
from api.endpoints import create_router

app = FastAPI()

# Initialize TithiService
tithi_service = TithiService()

# Create router with dependencies
api_router = create_router(tithi_service)
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
