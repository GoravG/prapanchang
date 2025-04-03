import logging
from services.tithi_service import calculate_tithi

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root(date):
    from utils.date_utils import get_date_from_string
    date = get_date_from_string(date)
    return calculate_tithi(date)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)