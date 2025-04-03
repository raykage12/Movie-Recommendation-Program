# Ray Min
# 03/14/2025
# Midterm Project - Movie System
import os
import re
from movie import Movie
from stack import Stack

# parse movie info  from the text files
def parse_movie_file(file_path):
    # read movie info from the file
    with open(file_path, 'r') as f:
        content = f.read()
    # get the movie attributes
    title_match = re.search(r'Title: (.+)', content)
    year_match = re.search(r'Year: (\d+)', content)
    genre_match = re.search(r'Genre: (.+)', content)
    rating_match = re.search(r'Rating: ([\d.]+)', content)

    # if all found create movie object and return
    if title_match and year_match and genre_match and rating_match:
        return Movie(title_match.group(1), year_match.group(1), genre_match.group(1), rating_match.group(1))
    return None

# scans the directory for movie files and adds them to stack
def load_movies(directory, movie_list):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                movie = parse_movie_file(os.path.join(root, file))
                if movie:
                    movie_list.push(movie)


def main():
    # initilize movie list using stack
    movie_list = Stack()
    # user enters directory and is then loaded into to the stack
    directory = input("Enter the top-level directory to scan: ")
    load_movies(directory, movie_list)

    print("\nWelcome to the Movie Recommendation System!\n\nMain Menu:")
    while True:
        # Main menu
        print("\n1. List all movies")
        print("2. Recommend a movie")
        print("3. Search for a movie by title")
        print("4. Recommend Top 3 movies by rating")
        print("5. Exit")
        choice = input("Enter choice: ")
        print()

        # if/else depending on user input
        if choice == "1":
            # list all movies
            for movie in movie_list.get_all():
                print(movie)
        elif choice == "2":
            # recommend random movie
            movie = movie_list.random_movie()
            print(f"Recommended Movie: {movie}")
        elif choice == "3":
            # search for movie by title
            title = input("Enter a movie title: ")
            found = [m for m in movie_list.get_all() if title.lower() in m.title.lower()]
            print("\n".join(map(str, found)) if found else "Movie not found")
        elif choice == "4":
            # gives top 3 rated movies
            top_movies = sorted(movie_list.get_all(), key=lambda x: x.rating, reverse=True)[:3]
            for movie in top_movies:
                print(movie)
        elif choice == "5":
            break
        else:
            print("Invalid Entry. Try Again")

if __name__ == "__main__":
    main()