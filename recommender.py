# in this file we have the code for the recommenders

import random

MOVIE_LIST= ['Prison break','Titanic','Money Heist','In the mood for love']

def random_recommender():
    ## describe the function!!!
    return random.sample(MOVIE_LIST, 1)


#def fancy_recommender():
#    ...

if __name__== "__main__":
    print(f"I recommend you to watch: {random_recommender()}")
