# 1. Write an application that prompts the user to enter a sequence of integer
#    numbers. If the user enters a number that has already been entered before,
#    the application should print all the numbers entered previously and term.

in = int(input())

arr = set()

while not in in arr:
    arr.add(in)
    in =int(input())
print(arr)
