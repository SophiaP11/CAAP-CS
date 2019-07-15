def main():
    print("This program will produce a sum of any series of numbers. Let's begin.")
    
    amount = eval(input("How many numbers are you wanting to be added together?  "))
    
    print("Now as prompted, please enter each number you would like to be summed together one at a time.")
    total =eval(input("What is your first number?  "))
   
    for i in range(1, amount):
        x = eval(input("What is your next number?  "))
        total = x + total 
            
    print("According to our calculations the sum of the", amount, "numbers you entered is", total, end=".")
    
main()