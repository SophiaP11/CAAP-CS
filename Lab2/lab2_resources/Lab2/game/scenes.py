# imports random madule form library
from random import randint

# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

#**************************************************************************************************************************

#**************************************************************************************************************************

class TheBeginning(Scene):
	name = "the_beginning"

	def enter(self):
		print("You wake up from a deep sleep and open your eyes. It's too dark to see anything and you can't remember how you got here or where you are.\nThe air is cold and sends a shiver up your spine. All you know is that you are not supposed to be here.\nAt once the rest of your senses awaken and you realize your throat is parched, your head is throbbing, and your stomach is clenching in hunger.\nYour body is barely responsive due to the lack of food and water. If you don't get out of here quick, you will die!")
		print("You feel around and discover a doorway, a bottle of water, and something that smells like food-perhaps some time of bread.")
		return self.action()
		
		
	def action(self):
		print ("What will you do?")
		choice = input("1) Drink the water. \n2) Eat the food(?). \n3) Eat the food and drink the water! \nchoice: ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("The cool water flows down your parched throat and instantly you feel better. The hunger still knaws at you, but your limbs don't feel like lead.\nGood thinking! A human can only survive 3 days without water and who knows how long you've been down here.\nWith your new found strength you drag yourself through the doorway.")
			return self.exit_scene('fire_room') # The user answered correctly and is being taken to the fire room scene.
		elif int(choice) == 2:
			print ("Your hunger overcomes you and quickly bite down on the food. Oh no! That's not food! In your blind hunger you mistook a chunk of something very unedible as food. \nYour already dry throat clenches all the way and you struggle to breath. \nYou gasp your last breath and your fingers brush against the water bottle. It sucks that its too late to drink it.")
			return self.exit_scene('death') # The user didn't answer correctly and is being taken to the death scene.
		elif int(choice) == 3:
			print ("Your hunger overcomes you and quickly bite down on the food. Oh no! That's not food! In your blind hunger you mistook a chunk of something very unedible as food. \nYour already dry throat clenches all the way and you struggle to breath. \nYou quicly chug the water in hopes that it help, but it is uesless. Whatever you ate is causing a deadly reaction nothing can fix. You gasp your last breath and pass out. ")
			return self.exit_scene('death') # The user didn't answer correctly and is being taken to the death scene.
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************

#**************************************************************************************************************************

class FireRoom(Scene):
	
	name = "fire_room"

	def enter(self):
		print("You stumble blindly into what seems to be a hallway. You see a faint glow outlinning a doorway ahead and rush to it.")
		print("AS you get closer the cold air fades to a pleasant warm. The air is thick and it chokes you up.\nYou hesitate.")
		return self.action()
		
		
	def action(self):
		print ("Should you open the door?")
		choice = input("1)Yeah. Where else is there to go? \n2) NO! \n3)Not yet...Maybe just investigate a bit further to know for sure. \nchoice: ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You touch the handle and it burns you. You jump back in surprise but it's too late. The door explodes outwards and hits you, throwing you against the other wall. \nYou feel searing pain as your whole body erupts into the flames reaching out from the doorway. \nThen everything goes dark.")
			return self.exit_scene('death') # The user answered correctly and is being taken to the next scene.
		elif int(choice) == 2:
			print ("You hurry past the door just as it explodes outwards. You feel the flames from within the room lick at your back as you flee down the hallway. That was a close call!")
			return self.exit_scene('hole') # The user answered correctly and is being taken to the hole scene.
		elif int(choice) == 3:
			print (" You pause for a second and connect the dots. The room beyond the doorway is on fire! You leap back in anticipation just as the door explodes outwards. \nUnfortunatly, flames roll out of the room blocking your way forward. Looks like your going to have to find a different way.")
			return self.exit_scene('locked_door') # The user answered correctly and is being taken to the locked door scene.
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************

#**************************************************************************************************************************

class LitHole(Scene):
	
	name = "lit_hole"

	def enter(self):
		print ("You continue along the hallway appreciating the light of the fire you just escaped from. You go towards what seems to be the end of the hallway and perhaps another doorway.")
		print ("You stop short however when you see a massive crater in the floor ahead. There is no way around it and upon further inspection it seems to be a long way down.")
		return self.action()

	def action(self):
		print ("what will you do?")
		choice = input("1) Run and Jump across. It looks like it could be a scaleable distance...Maybe?\n2) Climb down. The sides look climable and maybe you can just climb back up the other side. It just depends what's at the bottom...\n3) Try and inch around. It looks like there is about 6 inches of hallway still clinging to the sides of the walls. Maybe you could just tiptoe it?\nChoice: ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You walk back a few steps and take off running. As soon as you get to the edge of the ledge you jump.\n!!!\nOh no! The edge that you leap off of crumbles under the force and you lose your balance an momentum!\n You lurch forward and smash your head against the edge of the opposite side of the crater.")
			return self.exit_scene('death') # The user didn't answer correctly and is being taken to the death scene.
		elif int(choice) == 2:
			print ("You slowly pick you way down the hole. You test each step in case it crumbles-and some do. After an hour your foot hits the bottom and you step down.")
			return self.exit_scene('two_paths') # The user answered correctly and is being taken to the tunnel scene.
		elif int(choice) == 3:
			print ("You press yourself against the wall and inch your way across.\nWhen you get about halfway across, the edge your balancing on crumbles under the weight of one foot. You lose your balance and fall backwards.\nIt feels like the fall is forever, but it ends.\nIt ends suddenly and permanently as your entire body smashes against the bottom of the crater.")
			return self.exit_scene('death') # The user didn't answer correctly and is being taken to the death scene.
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************

#**************************************************************************************************************************

class LockedDoor(Scene):
	
	name = "locked_door"

	def enter(self):
		print ("You walk back towards the room you came from. Using your new source of light you discover a door you passed over. You try the handle and it's locked.\nThe light begins to dim as flames from the fire room burn out. However, underneath the handle you can still barely see an access keypad with numbers 0-9.")
		return self.action

	def action(self):
		print ("What do you do?")
		choice = input("1) Try and use the keypad to open the door.\n2) Kick the door down.\n3) Wait out the fire till you can get past it.\nChoice: ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("")
			return self.exit_scene('death') # The user didn't answer correctly and is being taken to the death scene.
		elif int(choice) == 2:
			print ("You slowly pick you way down the hole. You test each step in case it crumbles-and some do. After an hour your foot hits the bottom and you step down.")
			return self.exit_scene('two_paths') # The user answered correctly and is being taken to the tunnel scene.
		elif int(choice) == 3:
			print ("You press yourself against the wall and inch your way across.\nWhen you get about halfway across, the edge your balancing on crumbles under the weight of one foot. You lose your balance and fall backwards.\nIt feels like the fall is forever, but it ends.\nIt ends suddenly and permanently as your entire body smashes against the bottom of the crater.")
			return self.exit_scene('death') # The user didn't answer correctly and is being taken to the death scene.
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)
		
			code = [randint(0,9), randint(0,9), randint(0,9)]
			guesses = 0
			# loop to check three random integers, one at a time
			for i in range(3):
				print ("Enter digit %d." % (i+1))
				guess = input("[keypad]> ")
				if guess == ':q':
					return self.exit_scene(guess)
				try:
				   guess = int(guess)
				except ValueError:
				   print("That's not an int!")
				   return self.exit_scene(self.name)
				while int(guess) != code[i] and guesses <10:
					print ("BZZZZEDDD!")
					guesses += 1
					guess =input("[keypad]> ")
					if guess == ':q':
						return self.exit_scene(guess)
					try:
					   guess = int(guess)
					except ValueError:
					   print("That's not an int!")
					   guess = -1
		
		if guesses < 10:
			print ("The container clicks open and the seal breaks, letting gas out.")
			#raise ValueError ('todo')(change dialogue to reflect your own game.)
			return self.exit_scene('the_bridge')
		else:
			print ("The lock buzzes one last time and then you hear a sickening")
			#raise ValueError ('todo')(change dialogue to reflect your own game.)
			return self.exit_scene('death') # raise ValueError ('todo')

	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************

#**************************************************************************************************************************

class TwoPaths(Scene):
	
	name ='two_paths'

	def enter(self):
		raise ValueError ('todo')
	
	def action(self):
		raise ValueError ('todo')

	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************			

#**************************************************************************************************************************

class Tunnel(Scene):
	
	name ='tunnel'

	def enter(self):
		raise ValueError ('todo')
	
	def action(self):
		raise ValueError ('todo')

	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************

#**************************************************************************************************************************

class EscapePod(Scene):
	
	name = 'escape_pod'

	def enter(self):
		raise ValueError ('todo')


	def action(self):
		print ("There's 5 pods, which one do you take?")
		good_pod = randint(1,5)
		guess = input("[pod #]> ")

		if guess == ':q':
			return self.exit_scene(guess)
		try:
		   guess = int(guess)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)
		   
		if int(guess) != good_pod:
			print ("You jump into pod %s and hit the eject button."% guess)
			raise ValueError ('todo')
			return self.exit_scene('death')
		else:
			print ("You jump into pod %s and hit the eject button."% guess)
			raise ValueError ('todo')
			return self.exit_scene('finished')

	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************			

#**************************************************************************************************************************

class Finished(Scene):
	
	name ='finished'

	def enter(self):
		raise ValueError ('todo')
	
	def action(self):
		raise ValueError ('todo')

	def exit_scene(self, outcome):
		return outcome