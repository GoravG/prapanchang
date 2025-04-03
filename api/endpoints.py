from fastapi import APIRouter, Query
from datetime import date
from services.tithi_service import calculate_tithi
from schemas.date_schemas import DateInput

router = APIRouter()


@router.get("/panchanga")
async def get_panchanga(
    date: date = Query(default="2025-04-03", description="Date in YYYY-MM-DD format")
):
    """Get Tithi for a given date."""
    tithi = calculate_tithi(date)
    return {"panchanga": tithi}
