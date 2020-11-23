#function that takes in a number representing the temperature in Celsius and
#  returns the temperature in Fahrenheit and vice versa.

def fahrenheit_celsius(f):
    c = float(((f-32)*5)/9)
    return c

def celsius_fahrenheit(c):
    f = float ((9/5)* c + 32)
    return f

print("Select A to convert fahrenheit to celsius or ")
print("Select B to convert celsius to farenheit " )
option = input("Please enter your option: ").upper()
if option == "A":
    f = float(input("Please enter temperature in fahrenheit: "))
    print(fahrenheit_celsius(f))
elif option == "B":
    c = float(input("Please enter temperature in celsius: "))
    print (celsius_fahrenheit(c))
else:
    print("Enter correct options")
