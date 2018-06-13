import os
import json
from flask import Flask, render_template, request, redirect, url_for

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

def check_answer(riddle, answer):
    return riddle["answer"] == answer


@app.route("/")
def index():
    return render_template("index.html", players=load_players())


@app.route("/game/<player_url>/<riddle_number>", methods={"GET", "POST"})
def game(player_url, riddle_number):
    riddles = load_riddles()
    current_riddle = int(riddle_number) - 1
    next_riddle = current_riddle + 1

    if request.method == "POST":
        if check_answer(riddles[current_riddle], request.form["answer"]):
            return redirect(url_for('game', player_url=player_url, riddle_number=int(riddle_number)+1))

    return render_template("game.html", riddle=riddles[current_riddle], riddle_number=riddle_number)



if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('POST'),
            debug=True)
