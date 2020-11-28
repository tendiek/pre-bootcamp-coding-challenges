# function to convert any number into hours and minutes.
#(For example, 71 will become “1 hour, 11 minutes”)
def num_to_time(number):
    hours = number // 60
    minutes = number % 60
    if hours <= 1 and minutes <=1 :
        print(str(number) + " = " + str(hours) + " hour, " + str(minutes) + " minute")
    elif hours <= 1 and minutes >1:
        print(str(number) + " = " + str(hours) + " hour, " + str(minutes) + " minutes")
    elif hours > 1 and minutes <=1:
        print(str(number) + " = " + str(hours) + " hours, " + str(minutes) + " minute")
    else:
        print(str(number) + " = " + str(hours) + " hours, " + str(minutes) + " minutes")
    return

print("Program to convert numbers to time units. ")
number = int(input("Please enter number: "))
num_to_time(number)

