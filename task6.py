#function that takes in three numbers and returns the maximum number. Do this without using any builtin methods.
def find_max(x, y, z):
    my_list = [x, y, z]
    my_max =my_list[0]
    for number in my_list:
        if number > my_max:
            my_max =number
    return my_max

x = float(input("Please enter 1st number: "))
y = float(input("Please enter 2nd number: "))
z = float(input("Please enter 3rd number: "))
print(find_max(x, y, z))


