# Milestone Project - Riddle Game
## Practical Python

*Developer: sarahloh*

1. [Project Brief](#1.-project-brief)
2. [Technologies](#2.-technologies-and-dependencies)
4. [Workflow](#3.-workflow)
4. [UXD](#4.-uxd)
5. [Wireframes](#5.-wireframes)
6. [Testing](#6.-testing)
7. [Heroku Deployment](#7.-heroku-deployment)

### 1. Project Brief

In this project, you’ll be building a logic-driven application using the technologies that you have learned throughout Practical Python. You can either choose to use the example brief below or choose to use your idea for the website.

**CREATE A 'RIDDLE-ME-THIS' GUESSING GAME**

Build a web application game that asks players to guess the answer to a pictorial or text-based riddle.

- The player is presented with an image or text that contains the riddle. Players enter their answer into a textarea and submit their answer using a form.
- If a player guesses correctly they are redirected to the next riddle.
- If a player guesses incorrectly their incorrect guess is stored and printed below the riddle. The textarea is cleared so they can guess again.
- Multiple players can play an instance of the game at the same time. Users are identified by a unique username.
- Create a leaderboard that ranks top scores for all users.


### 2. Technologies and Dependencies

**Backend**

- [Python](https://www.python.org)
- [Flask](http://flask.pocoo.org)

**Frontend**

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
- [Bootstrap v4.1.0](https://getbootstrap.com/docs/4.1/)
- - https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css
- - https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js
- [Font Awesome v4.7.0](https://fontawesome.com/v4.7.0/)
- - https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css
- [jQuery v3.3.1](https://jquery.com)

**Version Control**

- [Git](https://git-scm.com)
- [Github](https://github.com)


### 3. Workflow

- Find riddles
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
- Create test.py
- Write a test in test.py
- Write the code to pass the test in run.py
- Continue writing tests and making them pass until you have all the functionality defined by UXD
- Make it look nice - complete Surface plane of UXD
- Deploy to Heroku (may need to install Heroku Toolbelt)


### 4. UXD

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

### 5. Wireframes

![Wireframes](https://raw.githubusercontent.com/sarahloh/p3-riddle-game/master/static/images/readme/wireframes.jpg)


### 6. Testing

<!--
[**HTML Validator Results**](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsarahloh.github.io%2Fp1-comeragh-equestrian%2F)

[**CSS Validator Results**](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fsarahloh.github.io%2Fp1-comeragh-equestrian%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
 -->

### 7. Heroku Deployment
