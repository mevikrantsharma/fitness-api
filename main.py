from fastapi import FastAPI
from routers import classes, bookings
import logging

app = FastAPI(title="Fitness Studio Booking API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fitness API!"}

# configure basic logging
logging.basicConfig(level=logging.INFO)

app.include_router(classes.router)
app.include_router(bookings.router)
