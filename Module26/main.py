from fastapi import FastAPI, HTTPException
import database
import models
from models import Recipe, RecipeCreate
import streamlit as st

app = FastAPI()
@app.get("/")
def read_root():
    return {"message", "Welcome to the Online Recipe Book CRUD API"}

@app.post("/recipes/", response_model=Recipe)
def create_recipe(recipe: Recipe):
    recipe_id = database.create_recipe(recipe)
    return models.Recipe(id=recipe_id, **recipe.dict())

@app.get("/recipes/", response_model=Recipe)
def read_recipe(recipe_id: int):
    recipe = database.read_recipe(recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe Not Found")
    return recipe

@app.put("/recipes/", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: RecipeCreate):
    updated = database.update_recipe(recipe_id, recipe)
    if not updated:
        raise HTTPException(status_code=404, detail="Recipe Not Found")
    return models.Recipe(id=recipe_id, **recipe.dict())


@app.delete("/recipes/", response_model=Recipe)
def delete_recipe(recipe_id: int):
    deleted = database.delete_recipe(recipe_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Recipe Not Found")
    return {"message": "Recipe Deleted Successfully"}
