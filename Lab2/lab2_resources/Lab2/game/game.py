# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ""
difficulty = 0
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
    global name
    global moves
    score = Score(name, moves)
    if won == True:
        print("You won!")
    else:
        print ("\nOH NO! You ran out of lives!")
    print ("Moves used:", moves)
    # if won == True:
    #     leaderboard.update(score)
    print ("\n   GAME OVER.\n")
    # leaderboard.print_board()
    name = ""
    moves = 0
    print ("\n*************************************************************\n")

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
    while True:
        global name 
        global moves 
        print ("Welcome to my game! To quit enter :q at any time. You will have three lives. Good luck!") # Explains to the user what you are running and how to exit the program if they need.
        name = input("\nLet's play! Please enter your name. > ") # assigns the name variable to the user's input of their name
        if (name == ':q'):
            exit(1)
        difficulty = input("Choose your difficulty by entering the amount of lives you would like to have. \n1-2:Pretty Hard \n3-4:So so \n5-6:Easy Peasy\nLives: ")
        if (difficulty == ':q'):
            exit(1)
        difficulty = eval(difficulty)
        a_map = Map('the_beginning') # Putting the user at the start scene
        a_game = Engine(a_map, difficulty)
        moves = a_game.play()
        game_over(a_game.won())

play_game()