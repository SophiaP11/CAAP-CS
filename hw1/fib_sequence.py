def main():
    print("This program is designed to tell you the number in the Fibonacci sequence you are wanting to index.")
    
    n = eval(input("Please indicate the POSITION of the number in the sequence for which you would like to know the value of. This postion should be a whole number reperesentation.   "))
    x=0
    y=1
    for i in range(1, n):
        x, y = y, x+y
    print(y)
    
main()