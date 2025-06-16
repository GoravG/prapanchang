from datetime import date
from typing import Any, Dict, List, Optional

from jyotisha.panchaanga.spatio_temporal import City
from jyotisha.panchaanga.temporal.time import Timezone

from app.constants.fasting import (
    CHATURTHI_RULES,
    FASTING_RULES,
    FESTIVAL_FASTING_RULES,
    TITHI_BASED_FASTS,
)
from app.constants.festivals import FESTIVAL_MAPPINGS

from .tithi_service import TithiService


class FestivalService:
    def __init__(self, timezone: str = "Asia/Kolkata", city: str = "Pune"):
        self.timezone = Timezone(timezone)
        self.city = City.get_city_from_db(city)
        self.tithi_service = TithiService(timezone=timezone, city=city)

    def _get_fasting_details(
        self, tithi_index: int, month_name: str, date_obj: date, festivals: List[str]
    ) -> List[str]:
        """Get fasting rules based on tithi index, month, weekday and festivals."""
        fasting_rules = []
        weekday = date_obj.strftime("%A")

        # Handle special Chaturthi cases
        if tithi_index in CHATURTHI_RULES:
            chaturthi_rule = CHATURTHI_RULES[tithi_index]
            fast_name = chaturthi_rule.get(weekday, chaturthi_rule["default"])
            fasting_rules.append(fast_name)
        # Handle other tithi-based fasts
        elif tithi_index in TITHI_BASED_FASTS and tithi_index in FASTING_RULES:
            fasting_rules.append(FASTING_RULES[tithi_index])

        # Check month-specific fasts
        month_key = (month_name, weekday)
        if month_key in FASTING_RULES:
            fasting_rules.append(FASTING_RULES[month_key])

        # Check festival-based fasts
        for festival in festivals:
            if festival in FESTIVAL_FASTING_RULES:
                fasting_rules.append(festival)

        return fasting_rules

    def get_festivals_for_date(
        self, date_obj: date, timezone: Optional[str] = None, city: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get festivals and fasting details for a given date."""
        try:
            # Get tithi details for the date
            tithi_details = self.tithi_service.calculate_tithi(date_obj, timezone, city)

            # Look up festivals based on month and tithi
            festivals = []
            key = (tithi_details["month_name"], tithi_details["tithi_name"])
            if key in FESTIVAL_MAPPINGS:
                festivals.append(FESTIVAL_MAPPINGS[key])

            fasting_rules = self._get_fasting_details(
                tithi_details["tithi"], tithi_details["month_name"], date_obj, festivals
            )

            return {
                "date": date_obj,
                "festivals": festivals,
                "fasting": fasting_rules,
                "tithi_details": tithi_details,
            }
        except Exception:
            raise
