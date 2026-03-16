import json
import os

FILENAME = "data.json"


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.
    """
    if not os.path.exists(FILENAME):
        return {}

    with open(FILENAME, "r") as file:
        return json.load(file)


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open(FILENAME, "w") as file:
        json.dump(movies, file, indent=4)


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it.
    """
    movies = get_movies()
    movies[title] = {"year": year, "rating": rating}
    save_movies(movies)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it.
    """
    movies = get_movies()
    if title in movies:
        del movies[title]
        save_movies(movies)


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it.
    """
    movies = get_movies()
    if title in movies:
        movies[title]["rating"] = rating
        save_movies(movies)