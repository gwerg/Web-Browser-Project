# List of movie titles
movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Forrest Gump", "Inception", "The Matrix", "Avengers: Infinity War", "Back to the Future", "The Lion King", "Pulp Fiction"]

# Ask the user for search terms
search_input = input("Enter movie title(s) to search for (separate multiple terms with spaces): ")

# Split the input into individual search terms
search_terms = search_input.split()

matches = []

for movie in movies:
    # Check if any of the search terms are in the movie title
    for term in search_terms:
        if term.lower() in movie.lower():
            matches.append(movie)
            break  
print("Search results:")
if matches:
    for match in matches:
        print(match)
else:
    print("No movies matched your search.")

print("Total results found:", len(matches))