import random
import difflib
import statistics


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
    print("9. Movies sorted by year")
    print("10. Filter movies")


def pause():
    input("\nPress enter to continue ")


def get_valid_rating(prompt):
    while True:
        value = input(prompt)
        try:
            rating = float(value)
            if 0 <= rating <= 10:
                return rating
            else:
                print("Rating must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid rating.")


def get_valid_year(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid year.")


def list_movies(movies):
    if not movies:
        print("No movies in database.")
        return

    print(f"\n{len(movies)} movies in total")
    for movie, data in movies.items():
        print(f"{movie} ({data['year']}): {data['rating']}")


def add_movie(movies):
    name = input("Enter new movie name: ")
    year = get_valid_year("Enter new movie year: ")
    rating = get_valid_rating("Enter new movie rating: ")
    movies[name] = {"year": year, "rating": rating}
    print(f"Movie {name} successfully added")


def delete_movie(movies):
    name = input("Enter movie name to delete: ")
    if name in movies:
        del movies[name]
        print(f"Movie {name} successfully deleted")
    else:
        print(f"Movie {name} doesn't exist!")


def update_movie(movies):
    name = input("Enter movie name: ")
    if name in movies:
        year = get_valid_year("Enter new movie year: ")
        rating = get_valid_rating("Enter new movie rating: ")
        movies[name]["year"] = year
        movies[name]["rating"] = rating
        print(f"Movie {name} successfully updated")
    else:
        print(f"Movie {name} doesn't exist!")


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
    print(f"Median rating: {median}")
    print(f"Best movie: {best}, {movies[best]['rating']}")
    print(f"Worst movie: {worst}, {movies[worst]['rating']}")


def random_movie(movies):
    if not movies:
        print("No movies available.")
        return

    movie = random.choice(list(movies.keys()))
    print(f"Your movie for tonight: {movie}, it's rated {movies[movie]['rating']}")


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


def sort_by_year(movies):
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["year"])
    for movie, data in sorted_movies:
        print(f"{movie} ({data['year']}): {data['rating']}")


def filter_movies(movies):
    while True:
        min_rating = input("Enter minimum rating (leave blank for no minimum rating): ")
        if min_rating == "":
            min_rating = 0
            break
        try:
            min_rating = float(min_rating)
            break
        except ValueError:
            print("Invalid input. Please enter a valid rating.")

    while True:
        min_year = input("Enter minimum year (leave blank for no minimum year): ")
        if min_year == "":
            min_year = 0
            break
        try:
            min_year = int(min_year)
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")

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
        choice = input("\nEnter choice (0-10): ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            list_movies(movies)
            pause()
        elif choice == "2":
            add_movie(movies)
            pause()
        elif choice == "3":
            delete_movie(movies)
            pause()
        elif choice == "4":
            update_movie(movies)
            pause()
        elif choice == "5":
            show_stats(movies)
            pause()
        elif choice == "6":
            random_movie(movies)
            pause()
        elif choice == "7":
            search_movie(movies)
            pause()
        elif choice == "8":
            sort_by_rating(movies)
            pause()
        elif choice == "9":
            sort_by_year(movies)
            pause()
        elif choice == "10":
            filter_movies(movies)
            pause()
        else:
            print("Invalid choice")
            pause()


if __name__ == "__main__":
    main()