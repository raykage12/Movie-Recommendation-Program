class Movie:
    def __init__(self, title, year, genre, rating):
        self.title = str(title)
        self.year = int(year)
        self.genre = str(genre)
        self.rating = float(rating)

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre} - Rating: {self.rating}"
    
