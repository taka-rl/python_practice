from flask import Flask


app = Flask(__name__)


def make_bold(function):
    def wrapper(*args, **kwargs):
        return '<b>' + function(*args, ** kwargs) + '</b>'
    return wrapper


def make_emphasis(function):
    def wrapper(*args, **kwargs):
        return '<em>' + function(*args, **kwargs) + '</em>'
    return wrapper


def make_underlined(function):
    def wrapper(*args, **kwargs):
        return '<u>' + function(*args, **kwargs) + '</u>'
    return wrapper


def make_h1(function):
    def wrapper(*args, **kwargs):
        return '<h1>' + function(*args, **kwargs) + '</h1>'
    return wrapper


@app.route("/")
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://www.theodysseyonline.com/media-library/image.gif?id=12859407&width=800&quality=80"width=200>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
@make_h1
def say_bye():
    return "Bye"


@app.route("/username/<path:name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)
