import random
import matplotlib.pyplot as plt
import difflib
import statistics


def print_menu():
    print("\nMenu:")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("9. Create rating histogram")



def get_valid_rating(prompt="Enter rating (0.0–10.0): "):
    while True:
        try:
            rating = float(input(prompt))
            if 0.0 <= rating <= 10.0:
                return rating
            print("Rating must be between 0.0 and 10.0")
        except ValueError:
            print("Please enter a valid number.")


def list_movies(movies):
    for movie, rating in movies.items():
        print(f"{movie}: {rating}")


def add_movie(movies):
    movie = input("Enter movie name: ")
    rating = get_valid_rating()
    movies[movie] = rating
    print("Movie added.")


def delete_movie(movies):
    movie = input("Enter movie to delete: ")
    if movie in movies:
        del movies[movie]
        print("Movie deleted.")
    else:
        print("Movie not found.")


def update_movie(movies):
    movie = input("Enter movie to update: ")
    if movie in movies:
        movies[movie] = get_valid_rating("Enter new rating (0–10): ")
        print("Movie updated.")
    else:
        print("Movie not found.")


def show_stats(movies):
    ratings = list(movies.values())

    avg = statistics.mean(ratings)
    median = statistics.median(ratings)

    best_movie = max(movies, key=movies.get)
    worst_movie = min(movies, key=movies.get)

    print(f"Average rating: {avg:.2f}")
    print(f"Median rating: {median:.2f}")
    print(f"Best movie: {best_movie} ({movies[best_movie]})")
    print(f"Worst movie: {worst_movie} ({movies[worst_movie]})")


def random_movie(movies):
    movie = random.choice(list(movies.keys()))
    print(f"{movie}: {movies[movie]}")


def search_movie(movies):
    query = input("Enter part of movie name: ").lower()

    matches = [
        movie for movie in movies
        if query in movie.lower()
    ]

    if matches:
        print("Matches found:")
        for movie in matches:
            print(f"{movie}: {movies[movie]}")
        return

    close_matches = difflib.get_close_matches(
        query, movies.keys(), n=5, cutoff=0.5
    )

    if close_matches:
        print("Did you mean:")
        for movie in close_matches:
            print(movie)
    else:
        print("No matching movies found.")


def sort_movies(movies):
    sorted_movies = sorted(
        movies.items(), key=lambda item: item[1], reverse=True
    )
    for movie, rating in sorted_movies:
        print(f"{movie}: {rating}")


def create_histogram(movies):
    filename = input("Enter filename (e.g. ratings.png): ")
    ratings = list(movies.values())
    colors = ["skyblue", "green", "orange", "purple", "red", "gold"]

    plt.figure()
    plt.hist(ratings, bins=10, edgecolor="black")
    plt.title("Movie Ratings Histogram")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    plt.grid(axis="y", alpha=0.5)
    plt.savefig(filename)
    plt.close()

    print(f"Histogram saved to {filename}")


def main():
    print(f"{'My Movies Database':*^50}")

    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    while True:
        print_menu()
        choice = input("Enter choice (1–10): ")

        if choice == "1":
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
            """
                   Search for a movie using exact or fuzzy matching.
                   Provides suggestions if an exact match is not found.

                   Reference implementation (for documentation only):

                       search = input("Enter part of movie name: ")
            """
            if search in movies:
                print(f"{search}: {movies[search]}")
            else:
                matches = difflib.get_close_matches(
                search, movies.keys(), n=5, cutoff=0.5
                )

                if matches:
                    print(f'The movie "{search}" does not exist. Did you mean:')
                    for match in matches:
                            print(match)
                    else:
                        print(f'The movie "{search}" does not exist. ' 'No suggestions found.' )
                        search_movie(movies)
                elif choice == "8":
                    sort_movies(movies)
                elif choice == "9":
                    create_histogram(movies)

                else:
                    print("Invalid choice.")


if __name__ == "__main__":
    main()