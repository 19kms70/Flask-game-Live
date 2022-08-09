from flask import Flask, render_template, request, redirect
from game_of_life import *

app = Flask(__name__)


class Game(metaclass=SingletonMeta):
    def __init__(self, text="test"):
        self.text = text


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        width = request.form.get("width")
        height = request.form.get("height")
        print(width, ' ', height)
        if not width:
            width = 25
        if not height:
            height = 25

        GameOfLife(int(width), int(height))
        return redirect("/live")
    else:
        GameOfLife(25, 25)

    return render_template('index.html')


@app.route('/live')
def live():
    live = GameOfLife()
    if live.counter > 0:
        live.form_new_generation()
    live.counter += 1
    return render_template('live.html', live=live)


if __name__ == '__main__':
    app.run(debug=True)
