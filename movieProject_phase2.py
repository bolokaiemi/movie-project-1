import random
import difflib
import statistics
import movie_storage
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


def list_movies():
      movies = movie_storage.get_movies()
      if not movies:
          print("No movies in database.")
          return

      print(f"\n{len(movies)} movies in total")
      for movie, data in movies.items():
          print(f"{movie} ({data['year']}): {data['rating']}")


def add_movie():
      movies = movie_storage.get_movies()
      title = input("Enter new movie name: ")

      if title in movies:
          print(f"Movie {title} already exists!")
          return

      try:
          year = int(input("Enter new movie year: "))
          rating = float(input("Enter new movie rating: "))
      except ValueError:
          print("Invalid input. Year must be integer, rating must be a number.")
          return

      movie_storage.add_movie(title, year, rating)
      print(f"Movie {title} successfully added")


def delete_movie():
      movies = movie_storage.get_movies()
      title = input("Enter movie name to delete: ")

      if title not in movies:
          print(f"Movie {title} doesn't exist!")
          return

      #confirm = input(f"Are you sure you want to delete '{title}'? (Y/N): ").lower()
      #if confirm != "y":
          #print("Delete cancelled.")
          #return

      movie_storage.delete_movie(title)
      print(f"Movie {title} successfully deleted")


def update_movie():
      movies = movie_storage.get_movies()
      title = input("Enter movie name to update: ")

      if title not in movies:
          print(f"Movie {title} doesn't exist!")
          return

      try:
          rating = float(input("Enter new movie rating: "))
      except ValueError:
          print("Invalid input. Rating must be a number.")
          return

      movie_storage.update_movie(title, rating)
      print(f"Movie {title} successfully updated")


def show_stats():
      movies = movie_storage.get_movies()
      if not movies:
          print("No movies in database.")
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


def random_movie():
      movies = movie_storage.get_movies()
      if not movies:
          print("No movies in database.")
          return

      movie = random.choice(list(movies.keys()))
      print(f"Your movie for tonight: {movie}, it's rated {movies[movie]['rating']}")


def search_movie():
      movies = movie_storage.get_movies()
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


def sort_by_rating():
      movies = movie_storage.get_movies()
      sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
      for movie, data in sorted_movies:
          print(f"{movie} ({data['year']}): {data['rating']}")


def create_histogram():
      movies = movie_storage.get_movies()
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


def sort_by_year():
      movies = movie_storage.get_movies()
      if not movies:
          print("No movies in database.")
          return

      while True:
          latest_first = input("Do you want the latest movies first? (Y/N) ").strip().lower()
          if latest_first in ("y", "n"):
              break
          print("Invalid input. Please enter Y or N.")

      reverse_order = True if latest_first == "y" else False

      sorted_movies = sorted(movies.items(), key=lambda x: x[1]["year"], reverse=reverse_order)
      for movie, data in sorted_movies:
          print(f"{movie} ({data['year']}): {data['rating']}")


def filter_movies():
      movies = movie_storage.get_movies()

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

      filtered = {m: d for m, d in movies.items() if d["rating"] >= min_rating and d["year"] >= min_year}

      if not filtered:
          print("No movies match the filter.")
          return

      for movie, data in filtered.items():
          print(f"{movie} ({data['year']}): {data['rating']}")


def main():
      while True:
          print_menu()
          choice = input("\nEnter choice (0-11): ")

          if choice == "0":
              print("Bye!")
              break
          elif choice == "1":
              list_movies()
              pause()
          elif choice == "2":
              add_movie()
              pause()
          elif choice == "3":
              delete_movie()
              pause()
          elif choice == "4":
              update_movie()
              pause()
          elif choice == "5":
              show_stats()
              pause()
          elif choice == "6":
              random_movie()
              pause()
          elif choice == "7":
              search_movie()
              pause()
          elif choice == "8":
              sort_by_rating()
              pause()
          elif choice == "9":
              create_histogram()
              pause()
          elif choice == "10":
              sort_by_year()
              pause()
          elif choice == "11":
              filter_movies()
              pause()
          else:
              print("Invalid choice")
              pause()


if __name__ == "__main__":
    main()