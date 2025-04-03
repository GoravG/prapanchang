from jyotisha.panchaanga.temporal.time import Date
from jyotisha.panchaanga.spatio_temporal import daily
from jyotisha.panchaanga.temporal import time
from jyotisha.panchaanga.spatio_temporal import City
from jyotisha.panchaanga.temporal.zodiac.angas import AngaType
from jyotisha.panchaanga.temporal.zodiac import NakshatraDivision, Ayanamsha
from app.constants import TITHI_NAMES, NAKSHATRA_NAMES, LUNAR_MONTH_NAMES

def calculate_tithi(date: Date) -> str:
	pune = City.get_city_from_db("Pune")
	jd = time.utc_gregorian_to_jd(Date(date.year, date.month, date.day))

	panch = daily.DailyPanchaanga.from_city_and_julian_day(
	city=pune, julian_day=jd)

	print(f"========Date: {panch.date}========")
	print(f'Tithi:{panch.sunrise_day_angas.tithi_at_sunrise.index}, Tithi Name: {TITHI_NAMES[panch.sunrise_day_angas.tithi_at_sunrise.index - 1]}')
	print(f'Nakshatra:{panch.sunrise_day_angas.nakshatra_at_sunrise.index}, Nakshatra Name: {NAKSHATRA_NAMES[panch.sunrise_day_angas.nakshatra_at_sunrise.index - 1]}')
	print(f'Month:{panch.lunar_month_sunrise.index}')
	print(f'==================================')

	return {
		"tithi": panch.sunrise_day_angas.tithi_at_sunrise.index,
		"tithi_name": TITHI_NAMES[panch.sunrise_day_angas.tithi_at_sunrise.index - 1],
		"nakshatra": panch.sunrise_day_angas.nakshatra_at_sunrise.index,
		"nakshatra_name": NAKSHATRA_NAMES[panch.sunrise_day_angas.nakshatra_at_sunrise.index - 1],
		"month": panch.lunar_month_sunrise.index,
		"month_name": get_month_name(panch.lunar_month_sunrise.index)
	}

def get_month_name(month_index):
    """Returns the name of the month based on its index."""
    prefix = ''
    if isinstance(month_index, float):
        month_index = int(month_index + 0.5)  # Convert float to nearest integer
        prefix = 'Adhika '
    return f'{prefix}{LUNAR_MONTH_NAMES[month_index - 1]}'