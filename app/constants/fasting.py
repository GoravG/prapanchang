CHATURTHI_RULES = {
    4: {"default": "Sankashti Chaturthi", "Tuesday": "Angaraki Sankashti Chaturthi"},
    19: {"default": "Vinayak Chaturthi", "Tuesday": "Angaraki Vinayak Chaturthi"},
}

FASTING_RULES = {
    # Tithi-based fasts (using tithi indices)
    11: "Ekadashi",  # Ekadashi
    19: "Sankashti Chaturthi",  # Chaturthi
    4: "Vinayak Chaturthi",  # Chaturthi
    8: "Ashtami",  # Ashtami
    # Month and weekday specific fasts
    ("Shravan", "Monday"): "Shravan Monday",
    ("Shravan", "Thursday"): "Shravan Thursday",
    ("Shravan", "Saturday"): "Shravan Saturday",
    ("Margashirsha", "Saturday"): "Margashirsha Saturday",
}

# Add festival-based fasting rules
FESTIVAL_FASTING_RULES = {
    "Datta Jayanti",
    "Navaratri",
    "Mahashivaratri",
    "Shreekrishna Janmashtami",
}

TITHI_BASED_FASTS = [4, 11, 13, 19]  # Both Chaturthis, Ekadashi, Trayodashi
