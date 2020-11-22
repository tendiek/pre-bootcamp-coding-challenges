# function to determine if a number is equals 65 or the 
# sum of two numbers equals 65
def my_func( x , y ):
    if (x == 65 or y == 65 or x + y == 65):
        return True
    else:
       return False  

x = int(input("Please enter 1st number: "))
y = int(input("Please enter 2nd number: "))
print(my_func(x,y))
