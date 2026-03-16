import json
import os

FILENAME = "movies.json"


def load_movies():
    if not os.path.exists(FILENAME):
        return {
            "In the Name of the Father": {"rating": 8.1, "year": 1993},
            "Titanic": {"rating": 7.9, "year": 1997},
            "The Shawshank Redemption": {"rating": 9.3, "year": 1994},
            "The Godfather": {"rating": 9.2, "year": 1972},
            "The Dark Knight": {"rating": 9.0, "year": 2008},
            "Schindler's List": {"rating": 8.9, "year": 1993},
            "Forrest Gump": {"rating": 8.8, "year": 1994},
            "Pulp Fiction": {"rating": 8.9, "year": 1994},
            "The Matrix": {"rating": 1.0, "year": 1999},
            "Fight Club": {"rating": 8.8, "year": 1999},
        }

    with open(FILENAME, "r") as file:
        return json.load(file)


def save_movies(movies):
    with open(FILENAME, "w") as file:
        json.dump(movies, file, indent=4)