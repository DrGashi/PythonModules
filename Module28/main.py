from fastapi import FastAPI, HTTPException
import database
import models
from models import Movie, MovieCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message", "Welcome"}

@app.post("/movies/", response_model=Movie)
def create_recipe(movie: Movie):
    movie_id = database.create_movie(movie)
    return models.Movie(id=movie_id, **movie.dict())

@app.get("/movies/", response_model=Movie)
def read_movie(movie_id: int):
    movie = database.read_movie(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie Not Found")
    return movie

@app.put("/movies/", response_model=Movie)
def update_movie(movie_id: int, movie: MovieCreate):
    updated = database.update_movie(movie_id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie Not Found")
    return models.Movie(id=movie_id, **movie.dict())


@app.delete("/movies/", response_model=Movie)
def delete_recipe(movie_id: int):
    deleted = database.delete_movie(movie_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Movie Not Found")
    return {"message": "Movie Deleted Successfully"}