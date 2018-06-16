import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def load_players():
    """
    Read players data from JSON file
    """
    with open("data/players.json", "r") as read_file:
        data = json.load(read_file)
        return data

def load_riddles():
    """
    Read riddles data from JSON file
    """
    with open("data/riddles.json", "r") as read_file:
        data = json.load(read_file)
        return data

def update_players(players):
    """
    Update the players JSON file with new score and/or availibity
    """
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

    # POST request
    if request.method == "POST":

        user_input = request.form["answer"]
        # Correct answer - go to next riddle
        if check_answer(riddles[current_riddle], user_input):
            return redirect(url_for('game', player_url=player_url, riddle_number=int(riddle_number)+1))

        # Incorrect answer - try again
        else:
            return render_template("game.html",
                                    riddle=riddles[current_riddle],
                                    riddle_number=riddle_number,
                                    incorrect_msg="'{0}' is not the right answer. Try again.".format(user_input))

    # GET request
    return render_template("game.html", riddle=riddles[current_riddle], riddle_number=riddle_number)


# To run on Heroku
if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('POST'),
            debug=True)

# To run in Cloud 9
# if __name__ == '__main__':
#     app.run(host=os.getenv('IP', '8080'),
#             port=os.getenv('PORT', '0.0.0.0'),
#             debug=True)
