import random
import difflib
import statistics
import matplotlib.pyplot as plt
import numpy as np


def print_menu():
    print("\nMenu:")
    print("0. Exit")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("9. Create rating histogram")
    print("10. Movies sorted by year")
    print("11. Filter movies")


def pause():
    input("\nPress enter to continue ")


def list_movies(movies):
    if not movies:
        print("No movies in database.")
        return

    print(f"\n{len(movies)} movies in total")
    for movie, data in movies.items():
        print(f"{movie} ({data['year']}): {data['rating']}")


# ✅ UPDATED add_movie
def add_movie(movies):
    name = input("Enter new movie name: ")

    for movie in movies:
        if movie.lower() == name.lower():
            print(f"Movie {movie} already exists!")
            return

    matches = difflib.get_close_matches(name, movies.keys())
    if matches:
        print("Did you mean one of these?")
        for m in matches:
            print(m)
        return

    year = int(input("Enter new movie year: "))
    rating = float(input("Enter new movie rating: "))

    movies[name] = {"year": year, "rating": rating}
    print(f"Movie {name} successfully added")


# ✅ UPDATED delete_movie
def delete_movie(movies):
    name = input("Enter movie name to delete: ")

    for movie in movies:
        if movie.lower() == name.lower():
            del movies[movie]
            print(f"Movie {movie} successfully deleted")
            return

    matches = difflib.get_close_matches(name, movies.keys())
    if matches:
        print("Did you mean:")
        for m in matches:
            print(m)
    else:
        print("Movie not found.")


# ✅ UPDATED update_movie
def update_movie(movies):
    name = input("Enter movie name: ")

    for movie in movies:
        if movie.lower() == name.lower():
            year = int(input("Enter new movie year: "))
            rating = float(input("Enter new movie rating: "))
            movies[movie]["year"] = year
            movies[movie]["rating"] = rating
            print(f"Movie {movie} successfully updated")
            return

    matches = difflib.get_close_matches(name, movies.keys())
    if matches:
        print("Did you mean:")
        for m in matches:
            print(m)
    else:
        print("Movie not found.")


def show_stats(movies):
    if not movies:
        print("No movies to show stats.")
        return

    ratings = [data["rating"] for data in movies.values()]
    avg = statistics.mean(ratings)
    median = statistics.median(ratings)

    best = max(movies, key=lambda m: movies[m]["rating"])
    worst = min(movies, key=lambda m: movies[m]["rating"])

    print(f"Average rating: {avg:.1f}")
    print(f"Median rating: {median:.1f}")
    print(f"Best movie: {best}, {movies[best]['rating']:.1f}")
    print(f"Worst movie: {worst}, {movies[worst]['rating']:.1f}")


def random_movie(movies):
    movie = random.choice(list(movies.keys()))
    print(f"Your movie for tonight: {movie}, it's rated {movies[movie]['rating']}")


# ❌ DO NOT TOUCH (you said keep it perfect)
def search_movie(movies):
    part = input("Enter part of movie name: ").lower()
    found = False

    for movie in movies:
        if part in movie.lower():
            data = movies[movie]
            print(f"{movie} ({data['year']}): {data['rating']}")
            found = True

    if not found:
        matches = difflib.get_close_matches(part, movies.keys())
        if matches:
            print("Did you mean:")
            for m in matches:
                print(m)
        else:
            print("Movie not found.")


def sort_by_rating(movies):
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
    for movie, data in sorted_movies:
        print(f"{movie} ({data['year']}): {data['rating']}")


# ✅ Choice 10 with Y/N
def sort_by_year(movies):
    latest_first = input("Do you want the latest movies first? (Y/N) ").strip().lower()
    reverse_order = True if latest_first == "y" else False

    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["year"], reverse=reverse_order)
    for movie, data in sorted_movies:
        print(f"{movie} ({data['year']}): {data['rating']}")


# ✅ Choice 9
def create_histogram(movies):
    filename = input("Enter filename to save histogram (e.g. ratings.png): ")

    ratings = [data["rating"] for data in movies.values()]
    colors = ["skyblue", "green", "orange", "purple", "red", "gold"]

    plt.figure()
    bins = np.arange(0, 11, 1)

    plt.hist(
        ratings,
        bins=bins,
        color=random.choice(colors),
        edgecolor="black",
        alpha=0.8
    )

    plt.title("Movie Ratings Histogram")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    plt.xticks(bins)
    plt.yticks(range(0, len(ratings) + 1))
    plt.grid(axis="y", alpha=0.5)
    plt.savefig(filename)
    plt.close()

    print(f"Histogram saved to {filename}")


def filter_movies(movies):
    min_rating = float(input("Enter minimum rating: "))
    min_year = int(input("Enter minimum year: "))

    for movie, data in movies.items():
        if data["rating"] >= min_rating and data["year"] >= min_year:
            print(f"{movie} ({data['year']}): {data['rating']}")


def main():
    movies = {
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

    while True:
        print_menu()
        choice = input("\nEnter choice (0-11): ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            list_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            update_movie(movies)
        elif choice == "5":
            show_stats(movies)
        elif choice == "6":
            random_movie(movies)
        elif choice == "7":
            search_movie(movies)
        elif choice == "8":
            sort_by_rating(movies)
        elif choice == "9":
            create_histogram(movies)
        elif choice == "10":
            sort_by_year(movies)
        elif choice == "11":
            filter_movies(movies)
        else:
            print("Invalid choice")

        pause()


if __name__ == "__main__":
    main()