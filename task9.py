#list all the natural numbers below 1000 that are multiples of 3 or 5.
#then sum this multiples
my_list =[]
count = 0
#number = int(input("Enter a number: "))
for i in range(1, 1000):
    if (i % 3 == 0 ) or (i % 5 == 0):
        my_list.append(i)
        add = sum(my_list)
        count += 1
print(my_list)
print("The sum of all numbers between 0 and 1000 divisable by 3 and 5 is: ", add)



