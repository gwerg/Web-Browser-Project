# List of movie titles
movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Forrest Gump", "Inception", "The Matrix", "Avengers: Infinity War", "Back to the Future", "The Lion King", "Pulp Fiction"]

# Ask the user for a search term
search = input("Enter a movie title to search for: ")

# Search for the movie by iterating over the list
for movie in movies:
    if search.lower() in movie.lower():
        print(f"Found: {movie}")
        break
    
else:    
    print(f"{search} not found.")
