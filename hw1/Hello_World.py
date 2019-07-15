def hello_world():

    print("Hello!")
    name = input("What is your name?  ")
    print("Nice to meet you", name , end="! ")
    age = input("How old are you? Please just enter a number.  ")
    live = input("Where do you live? Please enter: City, State.  ")
    travel = input("If you could go anywhere, where would you like to explore? Feel free to just list them like so: place1, place2, place3, etc. If you don't want to travel or explore anywhere just put 'nowhere'.  ")
    hobbies = input(" What do you enjoy doing? Please just list them like so: thing1, thing2, thing3, and thing4.  ")
    print("Thank you", name, "for your cooperation!")
    print("It seems that", age, "years has developed you into a wonderful person! I am very intrigued to hear that you live in", live, "yet you want to travel and explore", travel, end=". ")
    print("I'm so glad to hear you enjoy", hobbies, end="! The funny thing is, I do as well. We should meet up sometime! ")
    number = input("What is your number? ")
    print("Great! Maybe I will give you a call at", number, end=", or maybe I will just ghost you because I was totally lying about being interested in you.")
    print(" Goodbye!")
    
hello_world()
