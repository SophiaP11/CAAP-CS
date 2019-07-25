class Score(object):
	name = 'player'
	score = 0
	time = ""

	# initializes score and players name
	def __init__(self, name, score, time):
		self.name = name
		self.score = score
		self.time = time
	# returns the name associated with score
	def get_name(self):
		return self.name

	# returns score of player
	def get_score(self):
		return int(self.score)

	def get_time(self):
		return self.time
	