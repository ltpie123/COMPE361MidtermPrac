# 1. Write an application that prompts the user to enter a sequence of integer
#    numbers. If the user enters a number that has already been entered before,
#    the application should print all the numbers entered previously and term.

num_set = set()

usr_in = int(input())

while not usr_in in num_set:
    num_set.add(usr_in)
    usr_in = int(input())

print(num_set)
