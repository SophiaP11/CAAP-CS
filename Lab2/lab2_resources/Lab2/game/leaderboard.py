# imports the score class to be used in the leaderboard.
from scores import Score

#leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 10
	board = []

	def __init__(self):
		self.loading_leaderboard()
	# prints the leaderboard
	def print_board(self):
		print("\t\tLEADERBOARD:")
		for i in range(self.size):
			player = self.board[i]
			name, score, time = player.get_name(), player.get_score(), player.get_time()
			#gets the players name, score, and time and assigns each to the corresponding variables
			print("Player: ", name, "\tScore: ", score, "\tTime: ", time)

	# checks if given score should be in the leaderboard
	def update(self, score):
		for i in range(self.size):
			if score.get_score() <= self.board[i].get_score():
				Leaderboard().insert(score, i)
				break
				#stops the loop when it inserts the first time. It prevents it from replacing all scores of higher value in the leaderboard.

	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	def insert(self, score, place):
		self.board.insert(place, score)
		#inserts players score into the leaderboard

	def loading_leaderboard(self):
		#loads a leaderboard from previous game play to use for the current game
	    leaderboardfile = open("saved_leaderboard.txt", "r")
	    sleaderboard = leaderboardfile.read().splitlines()
	    for line in sleaderboard:
	    	name, moves, date, time = line.split(" ")
	    	score = Score(name, moves, str(date + " " + time))
	    	self.board.append(score)
	    self.size = len(sleaderboard)

	def saving_leaderboard(self):
		#sends the new leaderboard to an outside file to be saved and later used.
		leaderboardfile = open("saved_leaderboard.txt", "w")
		for i in range(self.size):
			name, score, time = self.board[i].get_name(), self.board[i].get_score(), self.board[i].get_time()
			print(name, score, time, file=leaderboardfile)

