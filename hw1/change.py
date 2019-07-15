def main():
    print("This will convert your exact change into the proper and least amount of each coin.")
    
    change = eval(input("What change do you need back?  "))
    
    change = change*100
    quarters = int(change / 25)
    change = change % 25
    dimes = int(change / 10)
    change = change % 10
    nickels = int(change / 5)
    change = change % 5
    pennies = int(change / 1)
    coins = int(quarters + dimes + nickels + pennies)
    
    print("You can get your exact change back in at least", coins, "coin/s/ with the following amounts of each type of coin.")
    print("Quarters:", quarters, "  Dimes:", dimes, "   Nickels:", nickels, "   Pennies", pennies)
    
main()