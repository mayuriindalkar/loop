a=5
i=1
while i<=5:
    n=int(input("enter number betn 1 to 10 : "))
    if a==n:
        print("you win, correct guess")
        break
    if a != n:
        print("You Losse")
    if a <= n:
        print("Low Number")
    if a >= n:
        print("High Number")
    i=i+1