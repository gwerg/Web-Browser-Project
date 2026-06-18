# List of movie titles
movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Forrest Gump", "Inception", "The Matrix", "Avengers: Infinity War", "Back to the Future", "The Lion King", "Pulp Fiction"]

# Ask the user for a search term
search_movie = input("Enter a movie title to search for: ")

matches = []

for movie in movies:
    if search_movie.lower() in movie.lower():
        matches.append(movie)
print("Search results:")
if matches:
    for match in matches:
        print(match)
else:
    print("No movies matched your search.")

print("Total results found:", len(matches))