from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    genre: str

class Movie(MovieCreate):
    id: int