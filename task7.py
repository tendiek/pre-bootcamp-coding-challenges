#function that takes in a number representing the temperature in Celsius and
#  returns the temperature in Fahrenheit and vice versa.

def fahrenheit_celsius(f):
    c = float(((f-32)*5)/9)
    return round(c,2)

def celsius_fahrenheit(c):
    f = float ((9/5)* c + 32)
    return round(f,2)

print("Select A to convert fahrenheit to celsius or ")
print("Select B to convert celsius to farenheit " )
print("Enter Q to quit")
option = " "
while option != "Q":
    try:
        option = input("Please enter your option: ").upper()
    except ValueError:
        break
    else:
        if option == "A":
            f = float(input("Please enter temperature in fahrenheit: "))
            print(fahrenheit_celsius(f))
        elif option == "B":
            c = float(input("Please enter temperature in celsius: "))
            print (celsius_fahrenheit(c))
        elif option == "Q":
            print("You have exited the program")
        else:
            print("Please select the correct option.")
