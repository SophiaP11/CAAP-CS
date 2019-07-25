# importing random int maker module
from random import randint

# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
	quips = ["Yep. You kinda suck at this.",
			"Your mom would be proud...",
			"Such a loser.",
			"Well that's embarrasing.",
			"I really thought you had it there. But nope.",
			"Better luck next time."
			# Things said to you when you lose the game.
			]
	def enter(self):
		print ("You died.")
		print (Death.quips[randint(0, len(self.quips)- 1)])
		return 'died'
		#tells the player they died and returns the died outcome back to the game engine.