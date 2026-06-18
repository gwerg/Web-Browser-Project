movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Forrest Gump", "Inception", "The Matrix", "Avengers: Infinity War", "Back to the Future", "The Lion King", "Pulp Fiction"]

last_query = None
last_results = None

print("Movie Search System")

while True:
    user_input = input("Enter search term(s): ").strip()
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    if user_input.lower() == 'last':
        print(" Previous Search History ")
        if last_query is None:
            print("No previous search history found.")
        else:
            print(f"Last Search Query: '{last_query}'")
            print(f"Results Found ({len(last_results)}):")
            for result in last_results:
                print(f"- {result}")
        continue

    search_terms = user_input.split()
    
    if not search_terms:
        print("Please enter at least one word to search.")
        continue

    matches = []

    for movie in movies:
        for term in search_terms:
            if term.lower() in movie.lower():
                matches.append(movie)
                break
    print("Search Results")
    if matches:
        for match in matches:
            print(f"- {match}")
    else:
        print("No movies matched your search.")
        
    print(f"Total results found: {len(matches)}\n")

    last_query = user_input
    last_results = matches