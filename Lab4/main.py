# Sophia Pegues
# Lab 4
# Sunday, August 4 


# Imports the turtle graphics module
import turtle
 
# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
turtle.screensize(200, 200, bg="#FFFFFF")
myPen = turtle.Turtle()
myPen.color("#000000")
myPen.speed(10)
# If you would like to slow down the animation, uncomment the next line. Higher delay, the slower it will be
turtle.delay(0)
# turtle.tracer(200)
# setting out box sizes to the n sq pixels per box
boxsize = 10
 

# myPen.setheading(n) points pen to given angle direction.
# where n equals the angle (think unit circle).
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
def goto_origin(myPen):
    myPen.penup()
    myPen.goto(-200, 200)
    myPen.pendown()
    return
# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    # Can also be done with a for loop - Can you rewrite thise function as such?
    myPen.begin_fill()
    for i in range(4):
        #moves the pen forward and then rotates 90 degrees
        myPen.forward(intDim)
        myPen.left(90)
    #At the end of loop the pen has rotated a total of 360 degrees and moved forward 4 times
    #In other words creates a box
    myPen.end_fill() 
    return
#This function draws a circle by using the circle function in turtle and the fill function
def circle(inDiameter):
    myPen.begin_fill()
    myPen.circle((inDiameter/2))
    myPen.end_fill()
    return
#This function draws a triangle by drawing each side of the triangle and using the fill function
def triangle(inLength):
    myPen.begin_fill()
    for i in range(3):
        myPen.forward(inLength)
        myPen.left(120)
    myPen.end_fill()
    return
# ######## Here is an example of how to draw a box using the box function      
# Comment these two lines out when you draw your own images ########
# box(boxSize)
# turtle.done()
 

#!!!!!!!! Challenge functions (2 bonus pts each) !!!!!!!!
# def save_image(): # saves the screen to an image/vector file
# You have a function for boxes, can you make functions for circles and triangles?
# def circle(intRadius):
# def triangle(intLength): #This can be an equilateral triangle, or not


# --------------------These are the instructions on how to move "myPen" around after drawing a box.----------------------
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the pen down and it draws as it moves, e.g.:
#:#:#:#:#:#:#:#:#:#:#:#:#:#:#:
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()
######################
 
# You will save your drawings in text files, which you will read from the art folder.
# You have two sample art pieces already saved. The first line will be a list of colors, and the 
# rest of the lines will be rows of pixels, which you should read and save as a list of lists.
# This first list stores the color values, e.g.:
# #FFFFFF,#FFFF00,#000000,#61380B,#F4FA58
# The drawings are stored using a "list of lists" structure where each value within every list
# element is the index of the color in the pallet list for that pixel

# This function will take in a filename path and load the art piece stored in that file.
# You are to parse the art into two lists, one for the color palette (first line of file),
# and a second with the pixel values (list of lists).
# The function returns both lists
def load_art(path):
    with open(path, "r") as artfile: #opens the file to reading status
        artfile = artfile.read().splitlines() #reads the lines one by one into a list for artfile
        pixels = []
        for line in artfile:
            if line == artfile[0]:
                pallet = line.split(",")
            else:
                pixelrow = line.split(",")
                pixels.append(pixelrow)
    return pallet, pixels




# This function takes a pallet and pixel list (matrix) to draw the picture
# It asks the user what shape they would like their pixels to be and then draws the art file.
def draw(pallet, pixels, boxsize):
    goto_origin(myPen)
    shape_number= int(input("What shape would you like your pixels to be?\n{1} Boxes\n{2} Triangles\n{3} Circles\n Choice: "))
    #changes the later statement {shape(boxsize)} to fit with the user's preferance
    try:
        if shape_number == 1:
            shape = box
        elif shape_number == 2:
            shape = triangle
        elif shape_number == 3:
            shape = circle
        for row in pixels: #each line of pixels
            for pixel in row: #each pixel in the line
                color = int(pixel)
                color = pallet[color]#assigns the color value of the pixel
                myPen.color(color) #changes the color of the pen to the correct color
                shape(boxsize) #draws the box
                myPen.penup() #stops the pen from drawing
                myPen.forward(boxsize) #moves the pen 1 pixel to the right
                myPen.pendown() #puts the pen down to start drawing again
            myPen.penup() #stops the pen from drawing
            myPen.right(90)#turns pen to face down
            myPen.forward(boxsize) #moves pen down 1
            myPen.left(90)#turns pen back up to face forward
            myPen.backward(len(row)*boxsize) #moves 1 len(line) back
            myPen.pendown() #puts the pen down to start drawing again
    except UnboundLocalError:
        print("Please make sure you are entering a number amongst the choices and just a number. I'm sorry but you will have to start over and reselect your art piece.")
        pixelart()
    return
# Should give the user a list of the possible drawing pieces you have and ask which one to draw
# After drawing the piece, asks the user if they would like to draw a different piece until they quit the program.
def pixelart():
    boxsize = 10
    choice = input("Which pixel art would you like to see? To quit enter :q.\n{1} Bannana\n{2} Mario\n{3} Pacman Ghost\n{4} Space Invader\n{5} Smiley Face\n{6} Mushroom\n{7} Panda\n{8} Aladdin Genie\nChoice: ")
    if (choice == ':q'):
        exit(1)
    else:
        while (choice != ':q'):
            try:
                goto_origin(myPen)
                choice = int(choice)
                if (choice == 1):
                    file = 'art/banana.txt'
                elif (choice == 2):
                    file = 'art/mario.txt'
                elif (choice == 3):
                    file = 'art/pacman.txt'
                elif (choice == 4):
                    file = 'art/alien.txt'
                    print(file)
                elif (choice == 5):
                    file = 'art/smileyface.txt'
                elif (choice == 6):
                    file = 'art/mushroom.txt'
                elif (choice == 7):
                    file = 'art/panda.txt'
                elif (choice == 8):
                    file = 'art/genie.txt'
                    boxsize = 5
                else:
                    print("Please make sure you are entering a number amongst the choices and just a number.")
                    pixelart()
                pallet_1, pixels_1 = load_art(file)
                turtle.resetscreen() #clears previous picture off the window
                turtle.tracer(300,0)
                draw(pallet_1, pixels_1, boxsize)
                turtle.update()
                boxsize = 10
                choice = input("Which pixel art would you like to see next? To quit enter :q.\n{1} Bannana\n{2} Mario\n{3} Pacman Ghost\n{4} Space Invader\n{5} Smiley Face\n{6} Mushroom\n{7} Panda\n{8} Aladdin Genie\nChoice: ")
            except ValueError:
                print("Please make sure you are entering a number amongst the choices and just a number.")
                pixelart()
        if (choice == ':q'):
            exit(1)
pixelart()
