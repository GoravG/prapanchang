# filepath: app/api/tithi_routes.py
from fastapi import APIRouter
from services.tithi_service import calculate_tithi

router = APIRouter()

@router.get("/")
async def get_tithi(date: str):
    """Get Tithi for a given date."""
    tithi = calculate_tithi(date)
    return {"date": date, "tithi": tithi}