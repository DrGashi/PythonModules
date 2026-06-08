from fastapi import FastAPI
from routers import mechanics, cars, api_key
from database import create_database

app = FastAPI(
    title="Book Management System",
    description="An API for managing books, authors, and genres.",
    version="1.0.0",
)

app.include_router(mechanics.router, prefix="/api/mechanics", tags=["Mechanics"])
app.include_router(cars.router, prefix="/api/cars", tags=["Cars"])
app.include_router(api_key.router, prefix="/api/validate_key")

@app.on_event("startup")
def startup():
    create_database()
