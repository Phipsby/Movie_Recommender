import csv
import random

# read in movies.csv file
MOVIES = {}
with open('movies.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    for row in reader:
        movie_id = int(row[0])
        movie_title = row[1]
        MOVIES[movie_id] = movie_title

# read in ratings.csv file
RATINGS = {}
with open('ratings.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    for row in reader:
        movie_id = int(row[1])
        rating = float(row[2])
        if movie_id not in RATINGS:
            RATINGS[movie_id] = []
        RATINGS[movie_id].append(rating)

def random_recommender():
    return random.choice(list(MOVIES.values()))

def popular_recommender():
    popular_movie_ids = [movie_id for movie_id in RATINGS.keys() if sum(RATINGS[movie_id]) / len(RATINGS[movie_id]) > 4.5]
    popular_movie_titles = [title for (movie_id, title) in MOVIES.items() if movie_id in popular_movie_ids]
    return random.choice(popular_movie_titles)

if __name__ == "__main__":
    print(f"I recommend you to watch: {random_recommender()}")
    print(f"I also recommend you to watch: {popular_recommender()}")
