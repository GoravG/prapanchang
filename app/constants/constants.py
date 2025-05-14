# app/core/constants.py

# Tithi names
TITHI_NAMES = [
    "Shukla Pratipada",  # 1
    "Shukla Dwitiya",  # 2
    "Shukla Tritiya",  # 3
    "Shukla Chaturthi",  # 4
    "Shukla Panchami",  # 5
    "Shukla Shashthi",  # 6
    "Shukla Saptami",  # 7
    "Shukla Ashtami",  # 8
    "Shukla Navami",  # 9
    "Shukla Dashami",  # 10
    "Shukla Ekadashi",  # 11
    "Shukla Dwadashi",  # 12
    "Shukla Trayodashi",  # 13
    "Shukla Chaturdashi",  # 14
    "Shukla Purnima",  # 15 (Full Moon)
    "Krushna Pratipada",  # 16
    "Krushna Dwitiya",  # 17
    "Krushna Tritiya",  # 18
    "Krushna Chaturthi",  # 19
    "Krushna Panchami",  # 20
    "Krushna Shashthi",  # 21
    "Krushna Saptami",  # 22
    "Krushna Ashtami",  # 23
    "Krushna Navami",  # 24
    "Krushna Dashami",  # 25
    "Krushna Ekadashi",  # 26
    "Krushna Dwadashi",  # 27
    "Krushna Trayodashi",  # 28
    "Krushna Chaturdashi",  # 29
    "Krushna Amavasya",  # 30 (New Moon)
]

# Paksha names
PAKSHA_NAMES = ["Shukla", "Krishna"]

# Nakshatra names
NAKSHATRA_NAMES = [
    "Ashwini",
    "Bharani",
    "Krittika",
    "Rohini",
    "Mrigashira",
    "Ardra",
    "Punarvasu",
    "Pushya",
    "Ashlesha",
    "Magha",
    "Purva Phalguni",
    "Uttara Phalguni",
    "Hasta",
    "Chitra",
    "Swati",
    "Vishakha",
    "Anuradha",
    "Jyeshtha",
    "Mula",
    "Purva Ashadha",
    "Uttara Ashadha",
    "Shravana",
    "Dhanishta",
    "Shatabhisha",
    "Purva Bhadrapada",
    "Uttara Bhadrapada",
    "Revati",
]

# Solar month names (Rashi)
SOLAR_MONTH_NAMES = (
    "Mesha",
    "Vrishabha",
    "Mithuna",
    "Karka",
    "Simha",
    "Kanya",
    "Tula",
    "Vrischika",
    "Dhanu",
    "Makara",
    "Kumbha",
    "Meena",
)

# LUNAR month names (Amanta system, starting with Chaitra)
LUNAR_MONTH_NAMES = (
    "Chaitra",  # 1
    "Vaishakha",  # 2
    "Jyeshtha",  # 3
    "Ashadha",  # 4
    "Shravana",  # 5
    "Bhadrapada",  # 6
    "Ashwina",  # 7
    "Kartika",  # 8
    "Margashirsha",  # 9
    "Pausha",  # 10
    "Magha",  # 11
    "Phalguna",  # 12
)

# Lunar month start and end definitions
MONTH_SYSTEM_TYPES = ["amanta", "purnimanta"]

# Degrees per nakshatra (total 360° / 27 nakshatras)
DEGREES_PER_NAKSHATRA = 360.0 / 27

# Degrees per tithi (total 360° / 30 tithis)
DEGREES_PER_TITHI = 360.0 / 30

# Degrees per rashi (total 360° / 12 zodiac signs)
DEGREES_PER_RASHI = 360.0 / 12
