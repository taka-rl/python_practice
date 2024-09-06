from flask import Flask
import random


INIT = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
CORRECT = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGR5ZDA5ejh6bXJjaGF6aWE5cWtqbDg2OHBhOWo3Mng3d216OG53bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13mLwGra9bNEKQ/giphy.gif"
LOW = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTU1NzY2Zmtnb3o5cng4ZGE1d2E1aTkzZG05NzExMTl6ZHU0bWQ1dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8Bbl0U61TN6DK/giphy.gif"
HIGH = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXpxcXQwZHB3N3poOWwwOHc4andzY2J4cDlxMmE0N3k3Znh0MHJmaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fnlXXGImVWB0RYWWQj/giphy.gif"

app = Flask(__name__)


def style_decorator(function):
    def wrapper(**kwargs):
        text = function(**kwargs)
        if function.__name__ == "check_number":
            if 'low' in text:
                text_color = "pink"
                git_link = LOW
            elif 'high' in text:
                text_color = "purple"
                git_link = HIGH
            else:
                text_color = "blue"
                git_link = CORRECT

        else:
            text_color = "black"
            git_link = INIT

        return f'<h1 style="color:{text_color}">{text}</h1><br><br><img src="{git_link}">'

    return wrapper


@app.route("/", endpoint='init_page')
@style_decorator
def init_page():
    return '<h1 style="text-align:center">Guess Number between 1 and 9!</h1>'


@app.route("/<int:n>")
@style_decorator
def check_number(n: int) -> str:
    if number == n:
        text = 'You found me!'
        return text
    elif number < n:
        text = 'Too high, try again!'
        return text
    elif number > n:
        text = 'Too low, try again!'
        return text


if __name__ == "__main__":
    number = random.randint(1, 9)
    print(number)
    app.run(debug=True)
