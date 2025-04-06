from fastapi import APIRouter, Query, Path
from datetime import date
from typing import Optional
from services.tithi_service import tithi_service
from schemas.date_schemas import DateInput
from jyotisha.panchaanga.spatio_temporal import City, daily
from jyotisha.panchaanga.temporal.time import Date as JDate
from jyotisha.panchaanga.temporal.time import Timezone

router = APIRouter(
    prefix="/v1",
    tags=["panchanga"],
    responses={404: {"description": "Not found"}},
)


@router.get("/panchanga")
async def get_panchanga(
    date: date = Query(default="2025-04-03", description="Date in YYYY-MM-DD format")
):
    """Get Tithi for a given date."""
    tithi = tithi_service.calculate_tithi(date)
    return {"panchanga": tithi}


@router.get("/calendars/coordinates/{latitude}/{longitude}/date/{date}")
async def get_panchanga_by_location(
    latitude: float = Path(..., description="Latitude of the location"),
    longitude: float = Path(..., description="Longitude of the location"),
    date: date = Path(..., description="Date in YYYY-MM-DD format"),
    timezone: str = Query(
        default="Asia/Kolkata", description="Timezone (e.g., Asia/Kolkata)"
    ),
):
    """Get panchanga details for a specific location and date."""
    city = City("", latitude, longitude, timezone)
    jdate = JDate(date.year, date.month, date.day)
    panchaanga = daily.DailyPanchaanga(city=city, date=jdate)

    return {
        "date": date.strftime("%Y-%m-%d"),
        "location": {
            "latitude": latitude,
            "longitude": longitude,
            "timezone": timezone,
        },
        "panchanga": {
            "sunrise": str(panchaanga.sunrise),
            "sunset": str(panchaanga.sunset),
            "tithi": panchaanga.sunrise_day_angas.tithi_at_sunrise.name,
            "nakshatra": panchaanga.sunrise_day_angas.nakshatra_at_sunrise.name,
            "yoga": panchaanga.sunrise_day_angas.yoga_at_sunrise.name,
            "karana": panchaanga.sunrise_day_angas.karana_at_sunrise.name,
        },
    }


@router.get("/timezone/{timezone}/date/{date}")
async def get_timezone_details(
    timezone: str = Path(..., description="Timezone (e.g., Asia/Kolkata)"),
    date: date = Path(..., description="Date in YYYY-MM-DD format"),
):
    """Get timezone specific details for a date."""
    tz = Timezone(timezone)
    jdate = JDate(date.year, date.month, date.day)
    jd = tz.local_time_to_julian_day(jdate)

    return {"date": date.strftime("%Y-%m-%d"), "timezone": timezone, "julian_day": jd}
