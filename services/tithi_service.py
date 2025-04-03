from utils.logger import logger
from jyotisha.panchaanga.temporal.time import Date
from jyotisha.panchaanga.spatio_temporal import daily
from jyotisha.panchaanga.temporal import time
from jyotisha.panchaanga.spatio_temporal import City
from app.constants import TITHI_NAMES, NAKSHATRA_NAMES, LUNAR_MONTH_NAMES


def get_daily_panchaanga(date: Date):
    pune = City.get_city_from_db("Pune")
    jd = time.utc_gregorian_to_jd(Date(date.year, date.month, date.day))
    panchanga = daily.DailyPanchaanga.from_city_and_julian_day(city=pune, julian_day=jd)
    return panchanga


def calculate_tithi(date: Date) -> str:
    panch = get_daily_panchaanga(date)
    sunrise_angas = panch.sunrise_day_angas

    formatted_date = date.strftime("%d-%m-%Y")
    logger.debug(
        f"Date: {formatted_date}, "
        f"Tithi Index: {sunrise_angas.tithi_at_sunrise.index}, Tithi Name: {TITHI_NAMES[sunrise_angas.tithi_at_sunrise.index - 1]}, "
        f"Nakshatra Index: {sunrise_angas.nakshatra_at_sunrise.index}, Nakshatra Name: {NAKSHATRA_NAMES[sunrise_angas.nakshatra_at_sunrise.index - 1]}, "
        f"Lunar Month Index: {panch.lunar_month_sunrise.index}"
    )

    return {
        "date": formatted_date,
        "tithi": sunrise_angas.tithi_at_sunrise.index,
        "tithi_name": TITHI_NAMES[sunrise_angas.tithi_at_sunrise.index - 1],
        "nakshatra": sunrise_angas.nakshatra_at_sunrise.index,
        "nakshatra_name": NAKSHATRA_NAMES[sunrise_angas.nakshatra_at_sunrise.index - 1],
        "month": panch.lunar_month_sunrise.index,
        "month_name": get_month_name(panch.lunar_month_sunrise.index),
    }


def get_month_name(month_index):
    """Returns the name of the month based on its index."""
    prefix = ""
    if isinstance(month_index, float):
        month_index = int(month_index + 0.5)  # Convert float to nearest integer
        prefix = "Adhika "
    return f"{prefix}{LUNAR_MONTH_NAMES[month_index - 1]}"
