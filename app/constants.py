# app/core/constants.py

# Tithi names
TITHI_NAMES = [
    "Pratipada",     # 1
    "Dwitiya",       # 2
    "Tritiya",       # 3
    "Chaturthi",     # 4
    "Panchami",      # 5
    "Shashthi",      # 6
    "Saptami",       # 7
    "Ashtami",       # 8
    "Navami",        # 9
    "Dashami",       # 10
    "Ekadashi",      # 11
    "Dwadashi",      # 12
    "Trayodashi",    # 13
    "Chaturdashi",   # 14
    "Purnima",       # 15 (Full Moon)
    "Pratipada",     # 1
    "Dwitiya",       # 2
    "Tritiya",       # 3
    "Chaturthi",     # 4
    "Panchami",      # 5
    "Shashthi",      # 6
    "Saptami",       # 7
    "Ashtami",       # 8
    "Navami",        # 9
    "Dashami",       # 10
    "Ekadashi",      # 11
    "Dwadashi",      # 12
    "Trayodashi",    # 13
    "Chaturdashi",   # 14
    "Amavasya"       # 15 (New Moon)
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
    "Meena"
)

# LUNAR month names (Amanta system, starting with Chaitra)
LUNAR_MONTH_NAMES = (
    "Chaitra",
    "Vaishakha", 
    "Jyeshtha", 
    "Ashadha", 
    "Shravana", 
    "Bhadrapada", 
    "Ashwina",
    "Kartika", 
    "Margashirsha",
    "Pausha",
    "Magha", 
    "Phalguna",
)

# Lunar month start and end definitions
MONTH_SYSTEM_TYPES = ["amanta", "purnimanta"]

# Degrees per nakshatra (total 360° / 27 nakshatras)
DEGREES_PER_NAKSHATRA = 360.0 / 27

# Degrees per tithi (total 360° / 30 tithis)
DEGREES_PER_TITHI = 360.0 / 30

# Degrees per rashi (total 360° / 12 zodiac signs)
DEGREES_PER_RASHI = 360.0 / 12