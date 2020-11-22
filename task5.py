#function that calculate the area of a triangle using herons formula
def area_of_triagle(x, y, z):
    s = (x+ y +z)/2
    area = (s*(s-x)*(s-y)*(s-z)) ** 0.5
    return (area)

x = int(input("Please enter 1st side of the triangle: "))
y = int(input("Please enter 2nd side of the triangle: "))
z = int(input("Please enter 3rd side of the triangle: "))
print (area_of_triagle(x, y, z))

