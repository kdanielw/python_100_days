from flask import Flask, render_template
import random
import datetime
import requests

GENDERIZE_ENDPOINT = "https://api.genderize.io?name="
AGEFY_ENDPOINT = "https://api.agify.io?name="
BLOG_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

def resquester(endpoint):
    response = requests.get(url=endpoint)
    data = response.json()
    return data

@app.route("/")
def home():
    actual_year = datetime.datetime.today().year
    random_number = random.randint(1, 10)
    return render_template("study.html", num=random_number, YYYY=actual_year)

@app.route("/guess/<string:name>")
def guess(name):
    ender_data = resquester(GENDERIZE_ENDPOINT+name)
    age_data = resquester(AGEFY_ENDPOINT+name)
    return render_template("guess.html", name=name, gender=ender_data["gender"], age=age_data["age"])

@app.route("/blog/<num>")
def blog(num):
    print(num)
    blog_data = resquester(BLOG_ENDPOINT)
    return render_template("blog.html", posts=blog_data)

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)