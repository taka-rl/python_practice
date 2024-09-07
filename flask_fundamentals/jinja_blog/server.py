from flask import Flask, render_template
from datetime import date
import random
import requests

AGIFY = "https://api.agify.io?name="
GENDER = "https://api.genderize.io?name="


app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = date.today().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<path:name>')
def get_api(name: str):
    age_url = f"https://api.agify.io?name={name}"
    gender_url = f"https://api.genderize.io?name={name}"

    age_response = requests.get(age_url)
    gender_response = requests.get(gender_url)

    if age_response.status_code == 200 and gender_response.status_code == 200:
        data_age = age_response.json()
        data_gender = gender_response.json()
        age = data_age["age"]
        gender = data_gender["gender"]
        return render_template("guess.html", name=name, age=age, gender=gender)
    else:
        if age_response.status_code == 401 or gender_response.status_code == 401:
            error = f"Error: Unauthorized. Check your api key"
        if age_response.status_code == 422 or gender_response.status_code == 422:
            error = f"Error: Unprocessable Content. Name is invalid"
        return render_template("guess_error.html", error=error)


@app.route('/blog/<num>')
def get_blog(num: int):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


