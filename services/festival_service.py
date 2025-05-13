from datetime import date
from typing import Any, Dict, Optional

from jyotisha.panchaanga.spatio_temporal import City
from jyotisha.panchaanga.temporal.time import Timezone

from app.constants.festivals import FESTIVAL_MAPPINGS

from .tithi_service import TithiService


class FestivalService:
    def __init__(self, timezone: str = "Asia/Kolkata", city: str = "Pune"):
        self.timezone = Timezone(timezone)
        self.city = City.get_city_from_db(city)
        self.tithi_service = TithiService(timezone=timezone, city=city)

    def get_festivals_for_date(
        self, date_obj: date, timezone: Optional[str] = None, city: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get festivals for a given date based on tithi and month."""
        try:
            # Get tithi details for the date
            tithi_details = self.tithi_service.calculate_tithi(date_obj, timezone, city)

            # Look up festivals based on month and tithi
            festivals = []
            key = (tithi_details["month"], tithi_details["tithi"])
            if key in FESTIVAL_MAPPINGS:
                festivals.append(FESTIVAL_MAPPINGS[key])

            return {
                "date": date_obj,
                "festivals": festivals,
                "tithi_details": tithi_details,
            }
        except Exception:
            raise
