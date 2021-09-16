a=5
i=1
while i<=5:
    n=int(input("enter number betn 1 to 10 : "))
    if a==n:
        print("you win, correct guess")
        break
    else:
       print("you lose")
    i=i+1