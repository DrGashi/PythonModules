import sqlite3
from models import Recipe, RecipeCreate


def create_connection():
    connection = sqlite3.connect("recipebook.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def create_recipe(recipe: Recipe):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO recipes (recipe, category) VALUES (?, ?)', (recipe.recipe, recipe.category))
    connection.commit()
    recipe_id = cursor.lastrowid
    connection.close()
    return recipe_id


def read_recipes():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM recipes')
    rows = cursor.fetchall()
    connection.close()
    recipes = [Recipe(id=row[0], recipe=row[1], category=row[2]) for row in rows]
    return recipes

def read_recipe(recipe_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM recipes WHERE id=?', (recipe_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return Recipe(id=row["id"], recipe=row["recipe"], category=row["category"])

def update_recipe(recipe_id: int, recipe: RecipeCreate) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE recipes SET recipe=?, category=? ", (recipe.recipe, recipe.category, recipe_id))
    connection.commit()
    connection.close()
    updated = cursor.rowcount
    return updated > 0

def delete_recipe(recipe_id:int) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM recipes WHERE id=?', (recipe_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0

create_table()