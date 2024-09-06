from flask import Flask
import random


app = Flask(__name__)


@app.route("/")
def init_page():
    return '<h1 style="text-align:center">Guess Number between 1 and 9!</h1>'


@app.route("/<int:n>")
def check_number(n: int) -> str:
    if number == n:
        return '<h1>You found me!</h1>' \
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGR5ZDA5ejh6bXJjaGF6aWE5cWtqbDg2OHBhOWo3Mng3d216OG53bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13mLwGra9bNEKQ/giphy.gif">'
    elif number < n:
        return '<h1>Too high, try again!</h1>' \
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXpxcXQwZHB3N3poOWwwOHc4andzY2J4cDlxMmE0N3k3Znh0MHJmaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fnlXXGImVWB0RYWWQj/giphy.gif">'
    elif number > n:
        return '<h1>Too low, try again!</h1>' \
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTU1NzY2Zmtnb3o5cng4ZGE1d2E1aTkzZG05NzExMTl6ZHU0bWQ1dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8Bbl0U61TN6DK/giphy.gif">'


if __name__ == "__main__":
    number = random.randint(1, 9)
    print(number)
    app.run(debug=True)
