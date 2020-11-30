# function that takes two numbers as input and determine if either of the numbers is 3 
# AND the sum of the numbers contains a 3.
def num_compare( x , y ):
    add =x + y
    if (x == 3 or y == 3) and ("3" in str(add)):
        return True
    else:
       return False  

x = int(input("Please enter 1st number: "))
y = int(input("Please enter 2nd number: "))
print(num_compare(x ,y ))
