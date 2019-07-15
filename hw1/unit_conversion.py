def main():
    
    print("This program tells you what your US currency is equal to in Euros.")
    
    dollars = eval(input("What is the value of your US currency?  "))
    euros = dollars * 0.886407
    print("$",dollars, " equals", "€", euros, end=".")
    
main()