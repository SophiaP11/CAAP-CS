def main():
    
    print("This program will convert tempeartures from Fahrenheit to Celcius and then inform you of this conversion 5 times for the sake of sounding repetitive.")
    
    fahrenheit = eval(input("What is the temperature in Fahrenheit?  "))
    celsius = (5/9)*(fahrenheit-32)
    
    for i in range(5):
        print(fahrenheit,"degrees Fahrenheit is the equivalent of", celsius, "degrees Celsius.")
        
main()