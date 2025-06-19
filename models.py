from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from dateutil import parser, tz

# Helper to parse ISO strings into timezone-aware datetimes
def parse_datetime(dt_str: str) -> datetime:
    dt = parser.isoparse(dt_str)
    return dt.astimezone(tz.gettz("UTC"))

class ClassCreate(BaseModel):
    name: str = Field(..., example="Yoga Flow")
    dateTime: str = Field(..., example="2025-06-15T10:00:00+05:30")
    instructor: str
    availableSlots: int

    def to_mongo(self):
        # convert to stored dict with UTC datetime
        utc_dt = parse_datetime(self.dateTime)
        return {
            "name": self.name,
            "dateTime": utc_dt,
            "instructor": self.instructor,
            "availableSlots": self.availableSlots,
        }

class ClassOut(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int

class BookingCreate(BaseModel):
    class_id: str
    client_name: str
    client_email: EmailStr

class BookingOut(BookingCreate):
    id: str = Field(..., alias="_id")
    bookedAt: datetime
