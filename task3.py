# function to determine if a number is equals 65 or the 
# sum of two numbers equals 65
def my_func( x , y ):
    if (x == 65 or y == 65 or x + y == 65):
        return True
    else:
       return False  

print(my_func(55, 10))
