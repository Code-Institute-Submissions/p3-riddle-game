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
    Update the players JSON file
    """
    with open("data/players.json", "w") as write_file:
        json.dump(players, write_file, indent=4)

def check_answer(riddle, answer):
    return riddle["answer"] == answer

def increment_score(player_url):
    players = load_players()
    for p in players:
        if p["url"] == player_url:
            p["score"] = p["score"] + 1
    update_players(players)

def reset_player(player_url):
    players = load_players()
    for p in players:
        if p["url"] == player_url:
            p["active"] = False
            p["score"] = 0
    update_players(players)

def set_player_active(player_url):
    players = load_players()
    for p in players:
        if p["url"] == player_url:
            p["active"] = True
    update_players(players)


"""
Views
"""

@app.route("/")
def index():
    return render_template("index.html", players=load_players())


@app.route("/game/<player_url>/<riddle_number>", methods={"GET", "POST"})
def game(player_url, riddle_number):

    set_player_active(player_url)

    riddles = load_riddles()
    current_riddle_index = int(riddle_number) - 1
    next_riddle_number = int(riddle_number) + 1

    # POST request
    if request.method == "POST":

        user_input = request.form["answer"]

        # Correct answer - store player score and go to next riddle or end game
        if check_answer(riddles[current_riddle_index], user_input):

            increment_score(player_url)

            # All riddles answered
            if current_riddle_index == len(riddles)-1:

                # Reset player
                reset_player(player_url)

                return redirect(url_for('index'))

            # Next riddle
            else:
                return redirect(url_for('game',
                                         player_url=player_url,
                                         riddle_number=next_riddle_number))

        # Incorrect answer - try again
        else:
            return render_template("game.html",
                                    riddle=riddles[current_riddle_index],
                                    riddle_number=riddle_number,
                                    incorrect_msg="'{0}' is not the right answer. Try again.".format(user_input))

    # GET request
    return render_template("game.html", riddle=riddles[current_riddle_index], riddle_number=riddle_number, players=load_players())


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
