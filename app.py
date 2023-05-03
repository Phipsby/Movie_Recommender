from flask import Flask, render_template, request
from recommender import random_recommender, popular_recommender

app= Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/recommendations")
def recommendations():
    form= request.args
    form_data=dict(form)
    results=random_recommender()
    results_popular=popular_recommender()
    return render_template("recommendations.html", movies=results, results_popular=results_popular, votes=form)


if __name__ == '__main__':
  app.run(debug = True)
