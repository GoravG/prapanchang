# filepath: app/schemas/date_schemas.py
from pydantic import BaseModel
from datetime import date


class DateInput(BaseModel):
    date: date
