import sqlite3
from models import Movie, MovieCreate


def create_connection():
    connection = sqlite3.connect("movies.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE movies(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def create_movie(movie: Movie):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO movies (title, genre) VALUES (?, ?)", (movie.title, movie.genre))
    connection.commit()
    movie_id = cursor.lastrowid
    connection.close()
    return movie_id

def read_movies():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM movies')
    rows = cursor.fetchall()
    connection.close()
    movies = [Movie(id=row[0], title=row[1], genre=row[2]) for row in rows]
    return movies

def read_movie(movie_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies WHERE id=?", (movie_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return Movie(id=row["id"], title=row["title"], genre=row["genre"])

def update_movie(movie_id: int, movie: MovieCreate) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE movies SET title=?, genre=? WHERE id=?", (movie.title, movie.genre, movie_id))
    connection.commit()
    connection.close()
    updated = cursor.rowcount
    return updated > 0

def delete_movie(movie_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM movies WHERE id=?", (movie_id, ))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0