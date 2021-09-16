# sum = 0
# n = int(input("enter the number : "))
# a = n
# while a > 0:
#     b = a % 10
#     sum = sum + b
#     a = a // 10
# if n % sum == 0:
#     print(n,"is harshad number")
# else:
#     print(n,"is not harshad number")


# a = "2/"
# b = "2/"
# c = "2017"
# print(a,b,c)

# a = int(input("enter the number: "))
# b = int(input("enter the number : "))
# if a > b:
#     print(a,"greater")
# else:
#     print(b,"less number")

# i = 10
# while i >= 1:
#     print(-i)
#     i = i - 1


# a = int(input("Enter the number : "))
# if a == 4:
#     print("yes")
# else:
#     print("no")


# n = int(input("enter the number : "))
# i = 0
# while n >= 0:
#     a = n % 10
#     i = i * 10 + a
#     n = n // 10
# print("revrce no is ",i)


i = int(input("Enter the number : "))
sum = 0
orig = i
while i > 0:
    sum = sum+(i%10)*(i%10)*(i%10)
    i = i // 10
if orig == sum:
    print("Armstrong number")
else:
    print("Number is not armstrong")

