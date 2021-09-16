import random
sum = 1
a = random.randint(0,10)
i = int(input("Enter Guees Number Between 1 and 10 : "))

while a != i:
    print("Your Gueesing Number Was :",i)
    print("Not Correct Try Again")
    i = int(input("Enter Guess Number Again : "))
    if a == i:
        print("Your Gueesing Number Was :",i)
        print("You Win")
    sum = sum + 1