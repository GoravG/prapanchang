from utils.logger import logger
from jyotisha.panchaanga.temporal.time import Date, Timezone
from jyotisha.panchaanga.spatio_temporal import daily as Daily
from jyotisha.panchaanga.spatio_temporal import City
from app.constants.constants import TITHI_NAMES, NAKSHATRA_NAMES, LUNAR_MONTH_NAMES
from jyotisha.panchaanga.temporal.festival.rules import RulesRepo
from jyotisha.panchaanga.temporal import names
from indic_transliteration import sanscript
from typing import Dict, Any, Optional
from datetime import date


class TithiService:
    def __init__(self, timezone: str = "Asia/Kolkata", city: str = "Pune"):
        self.timezone = Timezone(timezone)
        self.city = City.get_city_from_db(city)

    def get_daily_panchaanga(self, date_obj: date) -> Daily.DailyPanchaanga:
        """Get daily panchaanga for given date."""
        jd = self.timezone.local_time_to_julian_day(
            Date(date_obj.year, date_obj.month, date_obj.day)
        )
        return Daily.DailyPanchaanga.from_city_and_julian_day(
            city=self.city, julian_day=jd
        )

    def get_month_name(self, month_index: float) -> str:
        """Returns the name of the month based on its index."""
        prefix = ""
        if isinstance(month_index, float):
            month_index = int(month_index + 0.5)
            prefix = "Adhika "
        return f"{prefix}{LUNAR_MONTH_NAMES[month_index - 1]}"

    def get_samvatsara_name(self, panchanga: Daily.DailyPanchaanga) -> str:
        """Returns the name of the Samvatsara based on its index."""
        return Daily.DailyPanchaanga.get_samvatsara(
            panchanga, month_type=RulesRepo.TROPICAL_MONTH_DIR
        )

    def get_solar_details(self, panch: Daily.DailyPanchaanga) -> Dict[str, Any]:
        """Get solar-related details from panchaanga."""
        return {
            "solar_month": panch.solar_sidereal_date_sunset.month,
            "solar_month_day": panch.solar_sidereal_date_sunset.day,
            "solar_month_transition": panch.solar_sidereal_date_sunset.month_transition,
            "ayana": names.NAMES["AYANA_NAMES"]["sa"][sanscript.DEVANAGARI][
                panch.solar_sidereal_date_sunset.month % 12 + 1
            ],
        }

    def get_time_details(self, panch: Daily.DailyPanchaanga) -> Dict[str, str]:
        """Get time-related details from panchaanga."""

        def format_time(julian_day: float) -> str:
            try:
                local_time = self.timezone.julian_day_to_local_time(
                    julian_day, round_seconds=True
                )
                if not local_time:
                    return "N/A"

                # Convert to hours, minutes, seconds
                total_seconds = int(local_time.second)
                extra_minutes = total_seconds // 60
                adjusted_seconds = total_seconds % 60
                total_minutes = local_time.minute + extra_minutes

                # Adjust the time components
                adjusted_hour = local_time.hour + (total_minutes // 60)
                adjusted_minute = total_minutes % 60

                # Create new time object with adjusted values
                adjusted_time = Date(
                    year=local_time.year,
                    month=local_time.month,
                    day=local_time.day,
                    hour=adjusted_hour,
                    minute=adjusted_minute,
                    second=adjusted_seconds,
                )

                return adjusted_time.to_datetime().strftime("%I:%M %p")
            except Exception as e:
                logger.error(f"Error formatting time: {str(e)}")
                return "N/A"

        return {
            "sunrise": format_time(panch.jd_sunrise),
            "sunset": format_time(panch.jd_sunset),
        }

    def calculate_tithi(
        self, date_obj: date, timezone: Optional[str] = None, city: Optional[str] = None
    ) -> Dict[str, Any]:
        """Calculate tithi and related details for given date."""
        try:
            if timezone or city:
                temp_service = TithiService(
                    timezone=timezone or self.timezone._timezone_id,
                    city=city or self.city.name,
                )
                return temp_service._calculate_tithi_internal(date_obj)
            return self._calculate_tithi_internal(date_obj)
        except Exception as e:
            logger.error(f"Error calculating tithi: {str(e)}")
            raise

    def _calculate_tithi_internal(self, date_obj: date) -> Dict[str, Any]:
        """Internal method to calculate tithi details."""
        try:
            panch = self.get_daily_panchaanga(date_obj)
            sunrise_angas = panch.sunrise_day_angas

            logger.debug(
                f"Date: {date_obj}, "
                f"Tithi: {sunrise_angas.tithi_at_sunrise.index}, "
                f"Nakshatra: {sunrise_angas.nakshatra_at_sunrise.index}, "
                f"Month: {panch.lunar_month_sunrise.index}"
            )

            return {
                "date": date_obj,
                "tithi": sunrise_angas.tithi_at_sunrise.index,
                "tithi_name": TITHI_NAMES[sunrise_angas.tithi_at_sunrise.index - 1],
                "nakshatra": sunrise_angas.nakshatra_at_sunrise.index,
                "nakshatra_name": NAKSHATRA_NAMES[
                    sunrise_angas.nakshatra_at_sunrise.index - 1
                ],
                "month": panch.lunar_month_sunrise.index,
                "month_name": self.get_month_name(panch.lunar_month_sunrise.index),
                "samvatsara": self.get_samvatsara_name(panch),
                **self.get_solar_details(panch),
                **self.get_time_details(panch),
            }
        except Exception as e:
            logger.error(f"Error calculating tithi: {str(e)}")
            raise
