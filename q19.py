n = int(input("enter the number: "))
if n % 2 !=0:
    print("weird",n) 
if n % 2==0:
    if n >= 2 and n <= 5:
        print("not weird",n)
    elif n >= 6 and n <= 20:
        print("weird",n)
    elif n > 20:
        print("not weird",n)

# i = 70
# while i >= 0:
#     if i % 7 ==0:
#         print(i)
#     i = i - 1

# a = int(input("enter the number: "))
# sum = 0
# i = 1
# while sum < a:
#     if a % i ==0:
#         sum = sum + 1
#     i = i + 1
# if a == sum:
#     print(a,"perfect number")
# else:
#     print(a,"not perfect number")
