# This is the engine of the game, basically runs everything

class Engine(object):
	
	# global variables to keep track of game status and live count	
	escaped = False
	lives = 1

	# initializes the map in the game
	def __init__(self, scene_map, lives):
		self.scene_map = scene_map
		self.lives = lives
	# takes current scene, plays it, gets the next scene, and updates the game
	# should also return the number of moves the game takes in total
	def play(self):
		current_scene = self.scene_map.opening_scene()
		next_scene_name = ''
		checkpoint = current_scene
		n_moves = 1
		while (next_scene_name != 'finished' and self.lives > 0):
			print ("\n*******************************************************************") #seperates scenes
			next_scene_name = current_scene.enter()
			#assigns the return value(the next scene the player will go to) of the current scene to the next scene name variable
			if (next_scene_name == ':q'):
				exit(1)
			elif (next_scene_name == 'death'):
				#only applies if the player died
				checkpoint = current_scene
				#creates a checkpoint of the scene they were just on before they made the choice that killed them
				n_moves += 1
				#Adds a move to the move count
				current_scene = self.scene_map.next_scene(next_scene_name)
				#sends them to the death scene
			elif (next_scene_name == 'died'):
				self.lives -= 1
				if (self.lives > 0):
					print("\nREROUTING TO LAST CHECKPOINT")
					#tells the player they are being sent to the last checkpoint they reached (the last scene they were in)
				current_scene = checkpoint
			else:
				checkpoint = current_scene
				#saves the players postition to the checkpoint so they can come back if they die
				print("\nCHECKPOINT REACHED!")
				current_scene = self.scene_map.next_scene(next_scene_name)
				#gets the scene object from the next_scene function by sending the name of the next scene. It then assigns this object to the current scene variable
				n_moves += 1
				#Adds a move to the move count
		if (next_scene_name == 'finished'):
			self.escaped = True
			#changes the escaped variable to true so the program knows they won
		return n_moves

	# updates the variable to determine whether player won or failed.
	def won(self):
		return self.escaped
		#sends the value of self escaped to the game over function.

	def livesleft(self):
		return self.lives
		#unused function
		#it would tell how many lives the player had left after they won the game. I decided I didn't want to use it.