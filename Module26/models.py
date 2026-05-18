from pydantic import BaseModel

class RecipeCreate(BaseModel):
    recipe: str
    category: str

class Recipe(RecipeCreate):
    id: int
