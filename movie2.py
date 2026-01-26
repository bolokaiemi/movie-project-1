import random
import matplotlib.pyplot as plt
import difflib
import statistics
import numpy as np


def print_menu():
      """Display the main menu options to the user."""
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


def get_valid_rating(prompt="Enter rating (0–10): "):
      """Prompt the user for a valid numeric movie rating between 0 and 10."""
      while True:
          try:
              rating = float(input(prompt))
              if 0 <= rating <= 10:
                  return rating
              print("Rating must be between 0 and 10")
          except ValueError:
              print("Please enter a valid number.")


def list_movies(movies):
      """Print all movies with their ratings."""
      for movie, rating in movies.items():
          print(f"{movie}: {rating}")


def add_movie(movies):
      """Add a new movie and its rating to the database."""
      movie = input("Enter movie name: ")
      rating = get_valid_rating()
      movies[movie] = rating
      print("Movie added.")


def delete_movie(movies):
      """Delete a movie from the database if it exists."""
      movie = input("Enter movie to delete: ")
      if movie in movies:
          del movies[movie]
          print("Movie deleted.")
      else:
          print("Movie not found.")


def update_movie(movies):
      """Update the rating of an existing movie."""
      movie = input("Enter movie to update: ")
      if movie in movies:
          movies[movie] = get_valid_rating("Enter new rating (0–10): ")
          print("Movie updated.")
      else:
          print("Movie not found.")


def show_stats(movies):
      """Display average, median, best, and worst movie ratings."""
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
      """Select and display a random movie from the database."""
      movie = random.choice(list(movies.keys()))
      print(f"{movie}: {movies[movie]}")


def search_movie(movies):
      """
      Search for a movie using exact or fuzzy matching.
      Provides suggestions if an exact match is not found.
      """
      search = input("Enter part of movie name: ")

      # Exact match
      if search in movies:
          print(f"{search}: {movies[search]}")
          return

      # Fuzzy matching
      matches = difflib.get_close_matches(
          search, movies.keys(), n=5, cutoff=0.4
      )

      if matches:
          print(f'The movie "{search}" does not exist. Did you mean:')
          for movie in matches:
              print(movie)
      else:
          print(f'The movie "{search}" does not exist. No suggestions found.')


def sort_movies(movies):
      """Print movies sorted by rating in descending order."""
      sorted_movies = sorted(
          movies.items(), key=lambda item: item[1], reverse=True
      )
      for movie, rating in sorted_movies:
          print(f"{movie}: {rating}")


def create_histogram(movies):
      """Create and save a histogram of movie ratings."""
      filename = input("Enter filename to save histogram (e.g. ratings.png): ")
      ratings = list(movies.values())
      colors = ["skyblue", "green", "orange", "purple", "red", "gold"]

      plt.figure()

      # Float bins from 0 to 10 with step 1.0
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


def main():
      """Run the movie database application."""
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
          choice = input("Enter choice (1–9): ")

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
              search_movie(movies)
          elif choice == "8":
              sort_movies(movies)
          elif choice == "9":
              create_histogram(movies)
          else:
              print("Invalid choice.")


if __name__ == "__main__":
    main()
