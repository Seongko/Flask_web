# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request, redirect
import json

app = Flask("JobScraper")

def load_jobs():
    with open("jobs.json", "r", encoding="utf-8") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:

# /YOUR CODE

db = {}

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        results = db[keyword]
    else:
        indeed_jobs = load_jobs()
        results = []
        for job in indeed_jobs:
            if keyword.lower() in job["title"].lower():
                title = job["title"]
                company = job["company_name"]
                desc = job["description"]
                jobs = {
                    "title": title,
                    "company": company,
                    "description": desc,
                }
                results.append(jobs)

        db[keyword] = results
    return render_template("search.html", keyword = keyword, jobs = results)



@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword is not db:
        return redirect(f"/search?keyword={keyword}")


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run()

# /BLUEPRINT