# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine
from datetime import datetime as date

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ""
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won, difficulty):
    global name
    global moves
    global leaderboard
    time = str(date.now())
    score = Score(name, moves, time)
    #sends the players name, score, and time finished to the score class so the data can be manipulated later by the leaderboard.
    if won == True:
        print("You won!")
    else:
        print ("\nOH NO! You ran out of lives!")
    #Lets the player know if they won or why they lost
    moves = score.get_score()
    #gets the most recent score/moves of the player
    if won == True:
        leaderboard.update(score)
    moves = moves-(difficulty*100)
    #changes the value of moves to reflect the actual amount of moves they made and not their total score(lives included)
    print ("Choices made:", moves)
    #Tells the player how many choices they made and lets them know the game has ended.
    print ("\n\t\tGAME OVER.\n")
    leaderboard.print_board()
    #prints the leaderboard
    leaderboard.saving_leaderboard()
    #saves the current leaderboard outside of the game program so that it can be called back when the game program is restarted 
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
        print ("Welcome to Sophia's game! To quit enter :q at any time. The goal is to escape with the lowest score possible. Each choice you make adds one to your score. Be careful though. The shortest path may not be the safest path. Good luck!") 
        # Explains to the user what you are running and how to exit the program if they need.
        name = input("\nTo start please enter your name(no spaces please!).\nNAME: ") 
        # assigns the name variable to the user's input of their name
        if (name == ':q'):
            exit(1)
        difficulty = input("Choose your difficulty by entering the amount of lives you would like to have. Every life adds 100 points to your score.\n1-2:Pretty Hard\n3-4:Average\n5-6:Easy Peasy\nLives: ")#creating difficulty levels
        #lets the player choose their difficulty level based on the amount of lives they choose. The amount of lives will affect their final score to make the leaderboard more fair.
        if (difficulty == ':q'):
            exit(1)
        difficulty = eval(difficulty)
        while int(difficulty) > 6 or int(difficulty) < 1:
            if int(difficulty) > 6:
                print("I don't want the game to be boring... Input fewer lives.")
            else:
                print("How can you play the game if you aren't alive??? Input more lives please.")
            difficulty = input("Choose your difficulty by entering the amount of lives you would like to have. Every life adds 100 points to your score.\n1-2:Pretty Hard\n3-4:Average\n5-6:Easy Peasy\nLives: ")
            if (difficulty == ':q'):
                exit(1)
            difficulty = eval(difficulty)
        a_map = Map('the_beginning') # Putting the user at the start scene
        a_game = Engine(a_map, difficulty)
        #Sends the amount of lives the player chose as well as the map to the game engine.
        moves = a_game.play()
        moves = moves + (difficulty*100)
        #changes the players score/moves to reflect the amount of lives they chose.
        game_over(a_game.won(), difficulty)

play_game()
