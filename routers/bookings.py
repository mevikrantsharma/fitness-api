from fastapi import APIRouter, HTTPException, Query
from models import BookingCreate, BookingOut
from database import db
from bson import ObjectId, errors
from datetime import datetime

router = APIRouter(tags=["bookings"])

@router.post("/book", response_model=BookingOut)
async def book_spot(booking: BookingCreate):
    # Validate and convert class_id
    try:
        oid=ObjectId(booking.class_id)
    except errors.InvalidId:
        raise HTTPException(400, "Invalid class_id format")
    
    cls=await db.classes.find_one({"_id":oid})
    if not cls:
        raise HTTPException(404, "Class not found")
    if cls["availableSlots"] < 1:
        raise HTTPException(400, "No slots available")
    # decrement slots atomically
    updated = await db.classes.update_one(
        {"_id": oid, "availableSlots": {"$gt": 0}},
        {"$inc": {"availableSlots": -1}}
        )
    if updated.modified_count != 1:
        raise HTTPException(400, "Failed to book — try again")
    booking_doc = {
        "class_id": oid,
        "client_name": booking.client_name,
        "client_email": booking.client_email,
        "bookedAt": datetime.utcnow()
    }
    res = await db.bookings.insert_one(booking_doc)
    created = await db.bookings.find_one({"_id": res.inserted_id})
# ── stringify ObjectIds for response_model ────────────────────────────
    created["_id"] = str(created["_id"])
    created["class_id"] = str(created["class_id"])
    return created

@router.get("/bookings", response_model=list[BookingOut])
async def list_bookings(email: str = Query(..., alias="client_email")):
    cursor = db.bookings.find({"client_email": email})
    bookings = await cursor.to_list(length=100)
    # stringify IDs
    for b in bookings:
        b["_id"] = str(b["_id"])
        b["class_id"] = str(b["class_id"])
    return bookings
