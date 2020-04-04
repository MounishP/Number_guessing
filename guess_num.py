from random import randint
expected = randint(0,20)
count = 0
while count < 3:
    num = int(input("enter a number: "))
    if num > 20:
        print("out of bound")
        break
    if num == expected:
        print("You Won!!")
    elif num > expected:
        print("{} is greater than expected".format(num))
    elif num < expected:
        print("{} is lesser than expected".format(num))
    count += 1
if count == 3:
    print("Better luck next time")
    print("{} is the expected number".format(expected))