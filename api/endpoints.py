from fastapi import APIRouter, Query, Path
from datetime import date, time
from typing import Optional
from services.tithi_service import calculate_tithi
from schemas.date_schemas import DateInput
from jyotisha.panchaanga.spatio_temporal import City, daily
from jyotisha.panchaanga.temporal.time import Date as JDate
from jyotisha.panchaanga.temporal.time import Timezone
from jyotisha.panchaanga import temporal
from jyotisha.panchaanga.temporal.time import Date
from jyotisha.panchaanga.temporal.body import Graha
from jyotisha.panchaanga.temporal.zodiac.angas import AngaType, Anga
from app.constants import (
    TITHI_NAMES,
    NAKSHATRA_NAMES,
)
from services.tithi_service import get_month_name

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
    tithi = calculate_tithi(date)
    return {"panchanga": tithi}


# @router.get("/calendars/coordinates/{latitude}/{longitude}/date/{date}")
# async def get_panchanga_by_location(
#     latitude: float = Path(..., description="Latitude of the location"),
#     longitude: float = Path(..., description="Longitude of the location"),
#     date: date = Path(..., description="Date in YYYY-MM-DD format"),
#     timezone: str = Query(
#         default="Asia/Kolkata", description="Timezone (e.g., Asia/Kolkata)"
#     ),
# ):
#     """Get panchanga details for a specific location and date."""
#     city = City("", latitude, longitude, timezone)
#     jdate = JDate(date.year, date.month, date.day)
#     panchaanga = daily.DailyPanchaanga(city=city, date=jdate)
#     sunrise_angas = panchaanga.sunrise_day_angas
#     formatted_date = date.strftime("%Y-%m-%d")

#     return {
#         "date": formatted_date,
#         "location": {
#             "latitude": latitude,
#             "longitude": longitude,
#             "timezone": timezone,
#         },
#         "panchanga": {
#             "sunrise": str(panchaanga.sunrise),
#             "sunset": str(panchaanga.sunset),
#             "tithi": sunrise_angas.tithi_at_sunrise,
#             "tithi_name": TITHI_NAMES[sunrise_angas.tithi_at_sunrise.index - 1],
#             "nakshatra": sunrise_angas.nakshatra_at_sunrise,
#             "nakshatra_name": NAKSHATRA_NAMES[
#                 sunrise_angas.nakshatra_at_sunrise.index - 1
#             ],
#             "yoga": sunrise_angas.yoga_at_sunrise.index,
#             "karana": sunrise_angas.karana_at_sunrise,
#             "month": panchaanga.lunar_month_sunrise.index,
#             "month_name": get_month_name(panchaanga.lunar_month_sunrise.index),
#         },
#     }


# @router.get("/timezone/{timezone}/date/{date}")
# async def get_timezone_details(
#     timezone: str = Path(..., description="Timezone (e.g., Asia/Kolkata)"),
#     date: date = Path(..., description="Date in YYYY-MM-DD format"),
# ):
#     """Get timezone specific details for a date."""
#     tz = Timezone(timezone)
#     jdate = JDate(date.year, date.month, date.day)
#     jd = tz.local_time_to_julian_day(jdate)

#     return {"date": date.strftime("%Y-%m-%d"), "timezone": timezone, "julian_day": jd}


# @router.get(
#     "/timezones/{timezone}/times/years/{year}/months/{month}/days/{day}/hours/{hour}/minutes/{minute}/seconds/{second}/bodies/{body}/raashi_transition_100_days"
# )
# async def get_raashi_transition(
#     timezone: str = Path(..., description="Timezone (e.g., Asia/Kolkata)"),
#     year: int = Path(..., description="Year"),
#     month: int = Path(..., description="Month"),
#     day: int = Path(..., description="Day"),
#     hour: int = Path(..., description="Hour"),
#     minute: int = Path(..., description="Minute"),
#     second: int = Path(..., description="Second"),
#     body: str = Path(..., description="Planet (e.g., mars)"),
# ):
#     """Get Raashi transitions for a body over 100 days."""
#     jd = Timezone(timezone).local_time_to_julian_day(
#         Date(year, month, day, hour, minute, second)
#     )
#     transits = Graha.singleton(body).get_transits(
#         jd_start=jd,
#         jd_end=jd + 100,
#         anga_type=AngaType.RASHI,
#         ayanaamsha_id=Ayanamsha.CHITRA_AT_180,
#     )
#     transits_local = [
#         (
#             Timezone(timezone).julian_day_to_local_time(transit.jd),
#             transit.value_1,
#             transit.value_2,
#         )
#         for transit in transits
#     ]
#     return str(transits_local)
