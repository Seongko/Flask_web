# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request, redirect, send_file
import json
from file import save_to_file

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
                link = job["link"]
                jobs = {
                    "title": title,
                    "company": company,
                    "description": desc,
                    "link": link
                }
                results.append(jobs)

        db[keyword] = results
    return render_template("search.html", keyword = keyword, jobs = results)



@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run()

# /BLUEPRINT