import os
import json
from flask import Flask, render_template

app = Flask(__name__)


def load_players():
    with open("data/players.json", "r") as read_file:
        data = json.load(read_file)
        return data

def load_riddles():
    with open("data/riddles.json", "r") as read_file:
        data = json.load(read_file)
        return data

def update_players(players):
    with open("data/players.json", "w") as write_file:
        json.dump(players, write_file, indent=4)


@app.route("/")
def index():
    return render_template("index.html", players=load_players())


if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('POST'),
            debug=True)
