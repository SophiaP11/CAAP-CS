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
	#This is the first scene of the game.

	def enter(self):
		print("You wake up from a deep sleep and open your eyes. It's too dark to see anything and you can't remember how you got here or where you are.\nThe air is cold and sends a shiver up your spine. All you know is that you are not supposed to be here.\nAt once the rest of your senses awaken and you realize your throat is parched, your head is throbbing, and your stomach is clenching in hunger.\nYour body is barely responsive due to the lack of food and water. If you don't get out of here quick, you will die!")
		print("You feel around and discover a doorway, a bottle of water, and something that smells like food-perhaps some kind of bread.")
		return self.action()
		#calls the action scene for it's return value
		
		
	def action(self):
		print ("What will you do?")
		choice = input("1) Drink the water. \n2) Eat the food(?). \n3) Neither \nchoice: ")
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
			print ("\n\nThe cool water flows down your parched throat and instantly you feel better. The hunger still knaws at you, but your limbs don't feel like lead.\nGood thinking! A human can only survive 3 days without water and who knows how long you've been down here.\nWith your new found strength you drag yourself through the doorway.")
			return self.exit_scene('fire_room') # The user answered correctly and is being taken to the next scene.
		elif int(choice) == 2:
			print ("\n\nYour hunger overcomes you and quickly bite down on the food. Oh no! That's not food! In your blind hunger you mistook a chunk of something very unedible as food. \nYour already dry throat clenches all the way and you struggle to breath. \nYou gasp your last breath and your fingers brush against the water bottle. It sucks that its too late to drink it.")
			return self.exit_scene('death') # The user didn't answer correctly and is being taken to the death scene.
		elif int(choice) == 3:
			print ("\n\nYou stumble through the doorway with what little strength you have left. You barely make three steps out into the hallway before your body collapses of exhaustion.\n You immediatly regret your decision as your mind slips into oblivion.")
			return self.exit_scene('death') # The user didn't answer correctly and is being taken to the death scene.
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)
		#each choice sends the exit_scene the name of the next scene.

	def exit_scene(self, outcome):
		return outcome
		#the exit scene just sends the name of the next scene back to action, which sends back to enter.

#**************************************************************************************************************************

#**************************************************************************************************************************

class FireRoom(Scene):
	
	name = "fire_room"
	#This is the second scene of the game and is where the game storyline splits.

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
			print ("\n\nYou touch the handle and it burns you. You jump back in surprise but it's too late. The door explodes outwards, hits you, and throws you against the other wall.\nThen everything goes dark.")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("\n\nYou hurry past the door just as it explodes outwards. You feel the flames from within the room lick at your back as you flee down the hallway. That was a close call!")
			return self.exit_scene('lit_hole')
		elif int(choice) == 3:
			print ("\n\nYou pause for a second and connect the dots. The room beyond the doorway is on fire! You leap back in anticipation just as the door explodes outwards.\nUnfortunatly, flames roll out of the room blocking your way forward. Looks like your going to have to find a different way.")
			return self.exit_scene('locked_door')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************

#**************************************************************************************************************************

class LitHole(Scene):
	
	name = "lit_hole"

	#This a possible 3rd scene based on the choice in the second scene.

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
			print ("\n\nYou walk back a few steps and take off running. As soon as you get to the edge of the ledge you jump.\n!!!\nOh no! The edge that you leap off of crumbles under the force and you lose your balance an momentum!\n You lurch forward and smash your head against the edge of the opposite side of the crater.")
			return self.exit_scene('death') # The user didn't answer correctly and is being taken to the death scene.
		elif int(choice) == 2:
			print ("\n\nYou slowly pick you way down the hole. You test each step in case it crumbles-and some do. A half-hour later your foot hits the bottom and you step down.")
			return self.exit_scene('two_paths')
		elif int(choice) == 3:
			print ("\n\nYou press yourself against the wall and inch your way across.\nWhen you get about halfway across, the edge you're balancing on crumbles under the weight of one foot. You lose your balance and fall backwards.\nIt feels like the fall is forever, but it ends.\nIt ends suddenly and permanently as your entire body smashes against the bottom of the hole.")
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
	#This is a possible 3rd scene based on the choice made in the second scene.

	def enter(self):
		print ("You walk back towards the room you came from. Using your new source of light you discover a door you passed over. You try the handle and it's locked.\nThe light begins to dim as the flames from the room on fire burn out. However, underneath the handle you can still barely see an access keypad with numbers 0-9.")
		return self.action()

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
			print ("It looks like it's a 3 number code. It seems to only let you enter the next digit if the one before it is correct.")

			code = [int(1), randint(0,9), randint(0,9)]
			guesses = 0
			# loop to check three integers(two of them are random), one at a time
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
					print ("BZZZZEDDD! Looks like that was an incorrect value.")
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
					print ("\n\nThe keypad lights up, you hear a click, and a light turns on within the room. The door is unlocked!")
					#raise ValueError ('todo')(change dialogue to reflect your own game.)
					return self.exit_scene('two_choices')
			else:
				print ("\n\nThe keypad emits one last 'BZZZZEDDD' and then you hear a strange hissing sound. You realize it's releasing some type of gas. Your vision blurs and you pass out.")
				return self.exit_scene('death') # The user didn't answer correctly and is being taken to the death scene.

		elif int(choice) == 2:
			print ("\n\nYou rear back and slam your foot into the door.\nIt immediatly snaps in half. You vision blurs as you sink into the pool of your own blood.")
			return self.exit_scene('death') # The user answered correctly and is being taken to the death scene.
		elif int(choice) == 3:
			print ("\n\nYou head back towards the fire and wait until its died down enough so that you can cross the hallway safely. You pick your way carefully along but its incredibly difficult to see now that the fire is almost out.")
			return self.exit_scene('dark_hole') # The user answered correctly and is being taken to the dark_hole scene.
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)
		
			
	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************

#**************************************************************************************************************************

class TwoPaths(Scene):
	
	name ='two_paths'
	#This is the scene that comes after you decide to crawl down the hole.

	def enter(self):
		print("You feel along the wall and discover that there is a small opening leading somewhere. If you get on your hands and knees it seems big enough for you to fit.\nIt's as pitch black as the rest of your surroundings and shows no sign as a way out. But perhaps...\nThen again, you could always climb back up--in cold darkness--and get to that door you saw down the hallway.")
		return self.action()

	def action(self):
		print("What do you decide?")
		choice = input("1)Go the way you know and climb back up.\n2)Try the opening.\nchoice: ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("\n\nYou feel your way to the correct side and begin your extremely slow ascent in the cold darkness.\nYour fingers begin to numb.\nGripping the rocks becomes a struggle.\n You reach you hand up to grip the next rock, but its not sturdy enough and your numb fingers don't realize it. You crash to the bottom.")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("\n\nYou duck down and begin to crawl on your hands and knees into what seems to be a tunnel.")
			return self.exit_scene('tunnel') 
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************

#**************************************************************************************************************************

class TwoChoices(Scene):
	
	name ='two_choices'
	#This scene comes after you unlock the door in the locked door scene.

	def enter(self):
		print("You hesitate.")
		return self.action()

	def action(self):
		print("Do you continue through the door?")
		choice = input("1)Yeah I want to continue. There's actual light in this room.\n2)Nah I'll go back.\nchoice: ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("\n\nYou open the door and proceed into the next room.")
			return self.exit_scene('doors_room') 
		elif int(choice) == 2:
			print ("\n\nYou turn back and go towards the room that was on fire.")
			return self.exit_scene('dark_hole')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************

#**************************************************************************************************************************

class DoorsRoom(Scene):
	
	name ='doors_room'
	#This scene comes after you decide to go through the locked door. It also loops through to itself if you choose to go through a door within this scene.
	#The only way to exit this scene once you are in it is to choose choice 11 and go back.

	def enter(self):
		print("To your horror you walk into another room with multiple doors on every wall.")
		return self.action()

	def action(self):
		print("The doors are numbered 1-10. Which door do you choose?")
		choice = input("1)Door 1\n2)Door 2\n3)Door 3\n4)Door 4\n5)Door 5\n6)Door 6\n7)Door 7\n8)Door 8\n9)Door 9\n10)Door 10\n11)None?\nchoice: ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) <10 or int(choice) == 10:
			print ("\n\nYou open door", int(choice))
			return self.exit_scene('doors_room')
		elif int(choice) == 11:
			print ("\n\nYou turn back and go towards the room that was on fire.")
			return self.exit_scene('dark_hole')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************			

#**************************************************************************************************************************

class Tunnel(Scene):
	#This scene comes after you choose to go through the opening in the two paths scene.
	name ='tunnel'

	def enter(self):
		print("As you crawl your knees grow weak from the stress. It feels like hours, and just when you feel like you can't go any further you get to a point where the path diverges.")
		return self.action()

	def action(self):
		print("You discover you can either climb up a sketchy ladder, continue on to the right, or crawl back the way you came. You swear you can see light to the right. What do you do?")
		choice = input("1)Climb up the sketchy ladder.\n2)Crawl back.\n3) Go to the right.\nchoice: ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("\n\nYou struggle up a few steps and before you know it your at the top. You muster the remaining strength you have to shove the grate at the top away. You welcome the blinding light of day that floods through the tunnel. \nYou're free!!!!!!!")
			return self.exit_scene('finished')
		elif int(choice) == 2:
			print ("\n\nYou begin the long and awkward backwards crawl. Suddenly you hear a rumbling and before you know it the tunnel is collapsing.")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print("\n\nYou continue on to the right and discover you were right. There is light!\nYou surge forward, but just when you are about to escape you hear a rumble and the tunnel collapses.")
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************

#**************************************************************************************************************************

class DarkHole(Scene):
	
	name = "dark_hole"
	#This scene comes after you choose to go back towards the room that was on fire. It is the same location as the lit_hole scene, but reflects the later time in the game.

	def enter(self):
		print ("It's dark but you know you've passed the room that was on fire because of the smell and the crunch beneath your shoes. You continue on slowly down the dark hall hoping that an exit is near.")
		print ("You stop short however when your foot almost slips off into what you can only think to be a massive crater in the floor. Upon further careful inspection it seems there is no safe way around it. You drop a rock and you don't hear it land. It must be a long way down.")
		return self.action()

	def action(self):
		print ("what will you do?")
		choice = input("1) Run and Jump blindly across. \n2) Climb down. The sides feel climable and maybe you can just climb back up the other side. It just depends what's at the bottom...\n3) Try and inch around. It feels like there is about 6 inches of hallway still clinging to the sides of the walls. Maybe you could just tiptoe it?\nChoice: ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("\n\nYou walk back a few paces, take off running and jump.\nSomehow you make it to the other side!")
			return self.exit_scene('hallway_end') # The user didn't answer correctly and is being taken to the death scene.
		elif int(choice) == 2:
			print ("\n\nYou slowly pick your way down the hole. You test each step in case it crumbles-and some do. After an hour your foot hits the bottom and you step down.")
			return self.exit_scene('two_paths') # The user answered correctly and is being taken to the tunnel scene.
		elif int(choice) == 3:
			print ("\n\nYou press yourself against the wall and inch your way across.\nWhen you get about halfway across, the edge you're balancing on crumbles under the weight of one foot. You lose your balance and fall backwards.\nIt feels like the fall is forever, but it ends.\nIt ends suddenly and permanently as your entire body smashes against the bottom of the crater.")
			return self.exit_scene('death') # The user didn't answer correctly and is being taken to the death scene.
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************

#**************************************************************************************************************************

class HallwayEnd(Scene):
	
	name = 'hallway_end'
	#This scene comes after you choose to run and jump blindly over the hole in the dark_hole scene.

	def enter(self):
		print("You feel your way down the rest of the hallway till you stop at another door. It's locked!!! Luckly the keypad feels the same as the last one so you know how it works.")
		return self.action()

	def action(self):
		print ("What do you do?")
		choice = input("1) Try and use the keypad to open the door.\n2) Kick the door down.\n3) Turn back and climb down that stupid hole.\nChoice: ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("It looks like it's a 3 number code. It seems to only let you enter the next digit if the one before it is correct.")

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
					print ("BZZZZEDDD! Looks like that was an inccorrect value.")
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
					print ("\n\nThe keypad lights up and you hear a click. The door is unlocked! You push it open and, to your delight, are blinded by the light of day. You're free!!!!!")
					return self.exit_scene('finished')
			else:
				print ("\n\nThe keypad emits one last 'BZZZZEDDD' and then you hear a strange hissing sound. You realize it's releasing some type of gas. You pass out.")
				return self.exit_scene('death') 

		elif int(choice) == 2:
			print ("\n\nYou rear back and slam your foot into the door.\nIt immediatly snaps in half and you sink into the pool of your own blood.")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print ("\n\nYou turn back,find the hole, and begin your slow climb down. You test each step in case it crumbles-and some do. After an hour your foot hits the bottom and you step down.")
			return self.exit_scene('two_paths') 
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # The user entered a number that did not correspond with a choice and is being told they put in a wrong input. Then they are sent back to the choices to try again.
			return self.exit_scene(self.name)
		
			
	def exit_scene(self, outcome):
		return outcome

#**************************************************************************************************************************			

#**************************************************************************************************************************