from fastapi import APIRouter, HTTPException
from models import ClassCreate, ClassOut
from database import db
from bson import ObjectId
from datetime import datetime

router = APIRouter(prefix="/classes", tags=["classes"])

@router.post("", response_model=ClassOut)
async def create_class(cls: ClassCreate):
    doc = cls.to_mongo()
    result = await db.classes.insert_one(doc)
    created = await db.classes.find_one({"_id": result.inserted_id})
    created["_id"] = str(created["_id"])
    return created

@router.get("", response_model=list[ClassOut])
async def list_classes():
    now = datetime.utcnow()
    cursor = db.classes.find()
    classes = await cursor.to_list(length=100)
    for cls in classes:
        cls["_id"] = str(cls["_id"])
    return classes
