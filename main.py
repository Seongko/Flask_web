# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r", encoding="utf-8") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:

# /YOUR CODE

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    indeed_jobs = load_jobs()
    return render_template("search.html", keyword = keyword, jobs = indeed_jobs)

# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run()

# /BLUEPRINT