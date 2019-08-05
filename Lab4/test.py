def pixelart():
    choice = input("Which pixel art would you like to see? To quit enter :q.\n{1} Bannana\n{2} Mario\n{3} Pacman Ghost\n{4} Space Invader\n{5} Smiley Face\n{6} Mushroom\nChoice: ")
    if (choice == ':q'):
        exit(1)
    else:
        print("Moving Pen")
    while (choice != ':q'):
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
        print(choice)
        print(file)
        print("assigning pallet and pixel values")
        print("drawing picture")
        # You need this to prevent the window from closing after drawing
        choice = input("Which pixel art would you like to see next? To quit enter :q.\n{1} Bannana\n{2} Mario\n{3} Pacman Ghost\n{4} Space Invader\n{5} Smiley Face\n{6} Mushroom\nChoice: ")
    if (choice == ':q'):
        exit(1)
pixelart()

def draw(pallet, pixels, boxsize):
    goto_origin(myPen)
    shape_number= int(input("What shape would you like your pixels to be?\n{1} Box\n{2} Triangle\n{3} Circle\n Choice: "))
    if shape_number == 1:
        shape = box
    elif shape_number == 2:
        shape = triangle
    elif shape_number == 3:
        shape = circle
    print("shape:", shape)
    for row in pixels: #each line of pixels
        for pixel in row: #each pixel in the line
            color = int(pixel)
            color = pallet[color]#assigns the color value of the pixel
            myPen.color(color) 
            print("color: ", color)#changes the color of the pen to the correct color
            shape(boxsize)
            print("boxsize: ", boxsize)
            myPen.penup() #stops the pen from drawing
            myPen.forward(boxsize) #moves the pen 1 pixel to the right
            myPen.pendown() #puts the pen down to start drawing again
        myPen.penup() #stops the pen from drawing
        myPen.right(90)#turns pen to face down
        myPen.forward(boxsize) #moves pen down 1
        myPen.left(90)#turns pen back up to face forward
        myPen.backward(len(row)*boxsize) #moves 1 len(line) back
        myPen.pendown() #puts the pen down to start drawing again
    return

def load_art(path):
    with open(path, "r") as artfile: #opens the file to reading status
        artfile = artfile.read().splitlines() #reads the lines one by one into a list for artfile
        print("Artfile: ", artfile)
        pixels = []
        for line in artfile:
            if line == artfile[0]:
                pallet = line.split(",")
                print("pallet:\n", pallet)
            else:
                pixelrow = line.split(",")
                print("pixel row:\n", pixelrow)
                pixels.append(pixelrow)
                print("pixels list:\n", pixels)
    return pallet, pixels

def box(intDim):
    myPen.begin_fill()
    for i in range(4):
        #moves the pen forward and then rotates 90 degrees
        myPen.forward(intDim)
        myPen.left(90)
    #At the end of loop the pen has rotated a total of 360 degrees and moved forward 4 times
    #In other words creates a box
    myPen.end_fill() 
    return

def circle(inDiameter):
    myPen.begin_fill()
    myPen.circle((inDiameter/2))
    myPen.end_fill()
    return

def triangle(inLength):
    myPen.begin_fill()
    for i in range(3):
        myPen.forward(inLength)
        myPen.left(120)
    myPen.end_fill()
    return


def goto_origin(myPen):
    myPen.penup()
    myPen.goto(-200, 200)
    myPen.pendown()
    return
