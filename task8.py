# function to convert any number into hours and minutes.
#(For example, 71 will become “1 hour, 11 minutes”)
def num_to_time(number):
    hours = number // 60
    minutes = number % 60
    print(str(number) + " = " + str(hours) + " hour, " + str(minutes) + " minutes")
    return

print("Program to convert numbera to time units. ")
number = int(input("Please enter number: "))
num_to_time(number)

