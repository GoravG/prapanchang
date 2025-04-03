from fastapi import FastAPI

app = FastAPI()

from api.endpoints import router as api_router
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)