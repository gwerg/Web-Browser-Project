movies = [
    {
        "title": "The Shawshank Redemption", 
        "director": "Frank Darabont", 
        "year": 1994, 
        "genre": "Drama"
     },
    {
        "title": "The Godfather",
        "director": "Francis Ford Coppola", 
        "year": 1972, 
        "genre": "Crime, Drama"
        },
    {
        "title": "The Dark Knight", 
        "director": "Christopher Nolan", 
        "year": 2008, 
        "genre": "Action, Crime, Drama"
        },
    {
        "title": "Forrest Gump", 
        "director": "Robert Zemeckis", 
        "year": 1994, 
        "genre": "Drama, Romance"
        },
    {
        "title": "Inception", 
        "director": "Christopher Nolan", 
        "year": 2010, 
        "genre": "Action, Adventure, Sci-Fi"
        },
    {
        "title": "The Matrix", 
        "director": "Lana Wachowski, Lilly Wachowski", 
        "year": 1999, 
        "genre": "Action, Sci-Fi"
        },
    {
        "title": "Avengers: Infinity War", 
        "director": "Anthony Russo, Joe Russo", 
        "year": 2018, 
        "genre": "Action, Adventure, Sci-Fi"
        },
    {
        "title": "Back to the Future", 
        "director": "Robert Zemeckis", 
        "year": 1985,
        "genre": "Adventure, Comedy, Sci-Fi"
        },
    {
        "title": "The Lion King", 
        "director": "Roger Allers, Rob Minkoff", 
        "year": 1994, 
        "genre": "Animation, Adventure, Drama"
        },
    {
        "title": "Pulp Fiction", 
        "director": "Quentin Tarantino", 
        "year": 1994, 
        "genre": "Crime, Drama"
        },
    {
        "title": "Fight Club", 
        "director": "David Fincher", 
        "year": 1999, 
        "genre": "Drama"
        },
    {
        "title": "Interstellar", 
        "director": "Christopher Nolan", 
        "year": 2014, 
        "genre": "Adventure, Drama, Sci-Fi"
        },
    {
        "title": "Spirited Away", 
        "director": "Hayao Miyazaki", 
        "year": 2001,
        "genre": "Animation, Adventure, Family"
        },
    {
        "title": "La La Land", 
        "director": "Damien Chazelle", 
        "year": 2016, 
        "genre": "Comedy, Drama, Music, Horror"
        },
    {
        "title": "Jurassic Park", 
        "director": "Steven Spielberg", 
        "year": 1993, 
        "genre": "Action, Adventure, Sci-Fi"
        },
    {
        "title": "Titanic", 
        "director": "James Cameron", 
        "year": 1997, 
        "genre": "Drama, Romance"
        },
    {
        "title": "The Lord of the Rings: The Fellowship of the Ring", 
        "director": "Peter Jackson", 
        "year": 2001, 
        "genre": "Adventure, Drama, Fantasy"
        },
    {
        "title": "Star Wars: Episode IV - A New Hope", 
        "director": "George Lucas", 
        "year": 1977, 
        "genre": "Action, Adventure, Fantasy"
        },
    {
        "title": "Goodfellas", 
        "director": "Martin Scorsese", 
        "year": 1990, 
        "genre": "Biography, Crime, Drama"
        },
    {
        "title": "The Silence of the Lambs", 
        "director": "Jonathan Demme", 
        "year": 1991, 
        "genre": "Crime, Drama, Thriller"
        },
]

def search_movies(movies_list):
    field = input("Select a search field (title/director/year/genre): ").strip().lower()
    search_term = input("Enter a search term: ").strip().lower()

    valid_fields = ["title", "director", "year", "genre"]

    if field in valid_fields:
        fields_to_check = [field]
    else:
        fields_to_check = valid_fields

    results = []

    for movie in movies_list:
        for f in fields_to_check:
            val = str(movie[f]).lower()
            if search_term in val:
                results.append(movie)
                break 

    print("\nResults:")
    if results:
        for movie in results:
            print(f"{movie['title']}, Director: {movie['director']}, Year: {movie['year']}, Genre: {movie['genre']}")
    else:
        print("No results found.")

search_movies(movies)