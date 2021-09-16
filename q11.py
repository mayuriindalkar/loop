import random
b = 5
sum = 1
a = random.randint(0,3)

while b <= 5:
    i = int(input("Enter Guees Number Between 1 and 10 : "))
    if i != a:
        print("Your Gueesing Number Was :",i)
        print("Not Correct Try Again")
    if a > i:
        print("You Losse Your Guess Number Was Small")
    if a < i:
        print("Your Guess Number Was So High")    
    i = int(input("Enter Guess Number Again : "))
    if a == i:
        print("Your Gueesing Number Was :",i)
        print("You Win")
        break   
    sum = sum + 1


