# Milestone Project - Riddle Game
## Practical Python

*Developer: sarahloh*

1. [Project Brief](#1-project-brief)
2. [Technologies](#2-technologies-and-dependencies)
3. [Workspace](#3-workspace)
4. [Workflow](#4-workflow)
5. [UXD](#5-uxd)
6. [Wireframes](#6-wireframes)
7. [Testing](#7-testing)
8. [Heroku Deployment](#8-heroku-deployment)
9. [How To Deploy Locally](#9-how-to-deploy-locally)

### 1 Project Brief

In this project, you’ll be building a logic-driven application using the technologies that you have learned throughout Practical Python. You can either choose to use the example brief below or choose to use your idea for the website.

**CREATE A 'RIDDLE-ME-THIS' GUESSING GAME**

Build a web application game that asks players to guess the answer to a pictorial or text-based riddle.

- The player is presented with an image or text that contains the riddle. Players enter their answer into a textarea and submit their answer using a form.
- If a player guesses correctly they are redirected to the next riddle.
- If a player guesses incorrectly their incorrect guess is stored and printed below the riddle. The textarea is cleared so they can guess again.
- Multiple players can play an instance of the game at the same time. Users are identified by a unique username.
- Create a leaderboard that ranks top scores for all users.


### 2 Technologies and Dependencies

**Backend**

- [Python3](https://www.python.org)
- [Flask](http://flask.pocoo.org)

**Frontend**

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
- [Bootstrap v4.1.1](https://getbootstrap.com/docs/4.1/)
- [jQuery v3.3.1](https://jquery.com)

**Version Control**

- [Git](https://git-scm.com)
- [Github](https://github.com)


### 3 Workspace

**Operating System** - [macOS High Sierra](https://en.wikipedia.org/wiki/MacOS_High_Sierra)
**Package Manager** - [Homebrew](https://brew.sh)
**Editor** - [Visual Studio Code](https://code.visualstudio.com)
**Language** - [Python3](https://www.python.org)
**Microframework** - [Flask](http://flask.pocoo.org)
**Testing**	- [unittest](https://docs.python.org/3/library/unittest.html)

### 4 Workflow

- Find riddles and create riddles.json
- Create project directory with readme
- Create git repo
- Work on UXD up to Skeleton plane
- Create wireframes
- Setup Visual Studio for Python
- Install pip3
- Install flask
- Create requirements.txt
- Create run.py
- Get Flask app up and running
- Create players.json
- Experiment with reading and writing json
- Create test.py
- Write a test in test.py
- Write the code to pass the test in run.py
- Continue writing tests and making them pass until you have all the functionality defined by UXD
- Make it look nice - complete Surface plane of UXD
- Deploy to Heroku (may need to install Heroku Toolbelt)


### 5 UXD

#### Strategy

| Focus                                                       | User Needs                                                            | Business Objectives                             |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| _What are you aiming to achieve?_                           | Choose a player                                                       | Add a project to my portfolio                   |
|                                                             | Read a riddle and enter an answer                                     |  |
| _For whom?_                                                 | Try again if the answer is wrong                                      |  |
| _TARGET AUDIENCE:_                                          | See my score and rank on the leaderboard                              |  |
| Fans of Lord of the Ring / The Hobbit                       | Finish the game |  |
|                                                             | Play again |  |

#### Scope

| Focus                                                       | Functional Specification                                              | Content Requirements                            |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| _Which features?_                                           | Choose a player character from a list                                 | Select player dropdown and button               |
| _What’s on the table?_                                      | Display a riddle                                                      | Riddle text                                     |
|                                                             | Enter an answer                                                       | Answer input                                    |
|                                                             | Return incorrect answer                                               | Submit answer button                            |
|                                                             | Store player and score                                                | Incorrect answer text                           |
|                                                             | Show leaderboard of players and scores                                | Leaderboard                                     |
|                                                             | Update score and leaderboard                                          |  |
|                                                             | Keep track of available characters to choose from                     |  |

#### Structure

| Focus                                                       | Interaction Design                                                           | Information Architecture                                                                |
|-------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| _How is the information structured?_                        | _Where am I? / How did I get here? / What can I do here? / Where can I go?_  | _Organizational / Navigational schemas (tree / nested list / hub and spoke / dashboard)_|
|                                                             | Select a player > First riddle                                               | tree structure                                                                          |
| _How is it logically grouped?_                              | Riddle answer correct > Next riddle                                          | index > riddle<sub>1</sub> > riddle<sub>2</sub> > riddle<sub>n</sub> > end game         |
|                                                             | Riddle answer incorrect > Try a different answer                             |  |
|                                                             | Last riddle answer correct > End of game, play again?                        |  |
|                                                             |  |  |

#### Skeleton

| Focus                                                         | Interface Design         | Navigational Design  | Information Design  |
|---------------------------------------------------------------|--------------------------|----------------------|---------------------|
| _How will the information be represented?_                    | See wireframes           |                      |                     |
|                                                               |  |  |  |
| _How will the user navigate to the information and features?_ |  |  |  |
|                                                               |  |  |  |
|                                                               |  |  |  |
|                                                               |  |  |  |
|                                                               |  |  |  |

#### Surface

| Focus                                                       | Visual Design                       |
|-------------------------------------------------------------|-------------------------------------|
| What will the finished product look like?                   |  |
|                                                             |  |
| What colours, typography and design elements will be used?  |  |
|                                                             |  |
|                                                             |  |

### 6 Wireframes

![Wireframes](https://raw.githubusercontent.com/sarahloh/p3-riddle-game/master/static/images/readme/wireframes.jpg)


### 7 Testing

I used the **Test Before** approach to Test Driven Development, using Python's **unittest** class.

I created a file called test_riddle_game.py and wrote the first test (below) which failed.  Then I wrote a function in run.py to make the test pass.  I continued in this way until I had all of the functionality required to build the game.

---

*Test 1*

```python
def test_load_players(self):
        """
        Test to ensure we can read players list from json file
        """
        players = run.load_players()
        self.assertEqual(len(players),15)
```

*code in run.py*

```python
def load_players():
    """
    Read players data from JSON file
    """
    with open("data/players.json", "r") as read_file:
        data = json.load(read_file)
        return data
```

---

*Test 2*

```python
def test_load_riddles(self):
        """
        Test to ensure we can read riddles list from json file
        """
        riddles = run.load_riddles()
        self.assertEqual(len(riddles),6)
```

*code in run.py*

```python
def load_riddles():
    """
    Read riddles data from JSON file
    """
    with open("data/riddles.json", "r") as read_file:
        data = json.load(read_file)
        return data
```

---

*Test 3*

```python
def test_update_player(self):
    """
    Test to ensure we can update a player's status in players.json
    """
    players = run.load_players()
    players[0]["available"] = False
    run.update_players(players)
    self.assertEqual(run.load_players()[0]["available"], False)
```

*code in run.py*

```python
def update_players(players):
    """
    Update the players JSON file
    """
    with open("data/players.json", "w") as write_file:
        json.dump(players, write_file, indent=4)
```

---

*Test 4*

```python
def test_compare_answer(self):
    """
    Test to check if an inputted answer is correct or not
    """
    riddles = run.load_riddles()
    self.assertEqual(run.check_answer(riddles[0], "mountain"), True)
    self.assertEqual(run.check_answer(riddles[0], "river"), False)
```

*code in run.py*

```python
def check_answer(riddle, answer):
    return riddle["answer"] in answer.lower()
```

---

*Test 5*

```python
def test_reset_player(self):
    """
    Test to ensure we can reset a player's score and availability
    when they finish the game
    """
    players = run.load_players()
    players[0]["active"] = True
    run.increment_score(players[0]["url"])
    run.update_players(players)

    run.reset_player(players[0]["url"])
    self.assertEqual(run.load_players()[0]["active"], False)
    self.assertEqual(run.load_players()[0]["score"], 0)
```

*code in run.py*

```python
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
```

---



<!--
[**HTML Validator Results**](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsarahloh.github.io%2Fp1-comeragh-equestrian%2F)

[**CSS Validator Results**](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fsarahloh.github.io%2Fp1-comeragh-equestrian%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
 -->

### 8 Heroku Deployment

1. Create a new app 'hobbit-riddle-game' on heroku.com

2. Install [Heroku CLI](https://devcenter.heroku.com/categories/command-line)
    - $ brew install heroku/brew/heroku

3. Login to heroku with email abd password
    - $ heroku login

4. Check app is there
    - $ heroku apps

5. Add heroku remote
    - $ heroku git:remote -a hobbit-riddle-game

6. Add Procfile (this tells heroku what to do with the project)
    - $ echo web: python run.py > Procfile

7. Git commit and push to heroku remote
    - $ git add Procfile
    - $ git ci -m 'Add Profile for heroku deployment'
    - $ git push -u heroku master

8. Set up dynos
    - $ heroku ps:scale web=1

9. Setup config variables on heroku dashboard

    ![Config Variables](https://raw.githubusercontent.com/sarahloh/p3-riddle-game/master/static/images/readme/config-vars.png)

10. Restart dynos

    ![Restart Dynos](https://raw.githubusercontent.com/sarahloh/p3-riddle-game/master/static/images/readme/restart-dynos.png)


### 9 How To Deploy Locally

```console
$ git clone git@github.com:sarahloh/p3-riddle-game.git
$ cd p3-riddle-game
$ pip3 install -r requirements.txt
$ python3 run.py
```
App available at http://127.0.0.1:5000/



