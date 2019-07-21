# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 5
	board = []

	def __init__(self):
		for i in range(self.size):
			name = "random" + str(i+1)
			score = 500
			score = Score(name, score)
			self.board.append(score)
	# prints the leaderboard
	def print_board(self):
		for i in range(self.size):
			name, score = self.board[i].get_name(), self.board[i].get_score()
			print(name, score)

	# checks if given score should be in the leaderboard
	def update(self, score):
		raise ValueError ('todo')

	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	def insert(self, score, i):
		raise ValueError ('todo')

leaderboard = Leaderboard()
leaderboard.print_board()