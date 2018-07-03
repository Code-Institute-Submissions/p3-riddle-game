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
    return riddle["answer"] in answer.lower()


def increment_score(player_url):
    """
    Update player score, called when answer is correct
    """
    players = load_players()
    for p in players:
        if p["url"] == player_url:
            p["score"] = p["score"] + 1
    update_players(players)


def reset_player(player_url):
    """
    Returns a player's score to zero and active status to false
    """
    players = load_players()
    for p in players:
        if p["url"] == player_url:
            p["active"] = False
            p["score"] = 0
    update_players(players)


def set_player_active(player_url):
    """
    Changes a player's active status to true
    """
    players = load_players()
    for p in players:
        if p["url"] == player_url:
            p["active"] = True
    update_players(players)


def get_leaderboard_players():
    """
    Return a sorted list of active players beginning with highest score
    """
    players = [p for p in load_players() if p["active"] and p["score"] > 0]
    return sorted(players, key=lambda k: k["score"], reverse=True)


def get_player_by_url(player_url):
    """
    Return the player dict that corresponds to the provided player_url
    """
    return [player for player in load_players() if player["url"] == player_url]


def players_are_available():
    players = load_players()
    available_players = [player for player in players if player["active"] == False]
    if len(available_players) > 0:
        return True
    else:
        return False


"""
Views
"""

@app.route("/")
def index():

    # If all players have been chosen, reset player at top of the leaderboard
    if not players_are_available():
        reset_player(get_leaderboard_players()[0]["url"])

    return render_template("index.html", players=load_players(), leaderboard=get_leaderboard_players())

@app.route("/player/<player_url>")
def player(player_url):
    return render_template("player.html", leaderboard=get_leaderboard_players(), player=get_player_by_url(player_url))


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
                return redirect(url_for('end', player_url=player_url))

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
                                    incorrect_msg="'{0}' is not the right answer. Try again.".format(user_input),
                                    player=get_player_by_url(player_url),
                                    leaderboard=get_leaderboard_players())

    # GET request
    return render_template("game.html",
                            riddle=riddles[current_riddle_index],
                            riddle_number=riddle_number,
                            player=get_player_by_url(player_url),
                            leaderboard=get_leaderboard_players())


@app.route("/end/<player_url>")
def end(player_url):
    player = [player for player in load_players() if player["url"] == player_url][0]
    return render_template("end.html", player=player)


# To run on Heroku
if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=False)

# To run in Cloud 9
# if __name__ == '__main__':
#     app.run(host=os.getenv('IP', '8080'),
#             port=os.getenv('PORT', '0.0.0.0'),
#             debug=True)
