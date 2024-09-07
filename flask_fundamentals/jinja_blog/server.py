from flask import Flask, render_template
from datetime import date
import requests
from post import Post

app = Flask(__name__)

current_year = date.today().year
all_posts = requests.get(url="https://api.npoint.io/813c044d51e8707883ea").json()


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
        error = f'error happened'
        if age_response.status_code == 401 or gender_response.status_code == 401:
            error = f"Error: Unauthorized. Check your api key"
        if age_response.status_code == 422 or gender_response.status_code == 422:
            error = f"Error: Unprocessable Content. Name is invalid"
        return render_template("guess_error.html", error=error)


@app.route('/post/<int:id_num>')
def get_post(id_num):
    for post_data in all_posts:
        if post_data["id"] == id_num:
            post = Post(post_data["id"],
                        post_data["title"],
                        post_data["subtitle"],
                        post_data["body"])
            print(post.id)
            return render_template("post.html", post=post)
    else:
        return None


@app.route('/blog')
def blog():
    return render_template("blog.html", posts=all_posts, year=current_year)


@app.route('/')
def home():
    return render_template("index.html", year=current_year)


if __name__ == "__main__":
    app.run(debug=True)


