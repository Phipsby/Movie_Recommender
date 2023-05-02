# in this file we have the code for the recommenders

import random
import csv

with open('movies.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    MOVIE_LIST = [movie[1] for movie in reader]

def random_recommender():
    ## describe the function!!!
    return random.sample(MOVIE_LIST, 1)


#def fancy_recommender():
#    ...

if __name__== "__main__":
    print(f"I recommend you to watch: {random_recommender()}")
