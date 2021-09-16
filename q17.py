# a = int(input("enter number : "))
# sum = 0
# i = 1
# while sum < a:
#     if a % i == 0:
#         sum = sum + i
#     i = i + 1
# if a == sum:
#     print("number is perfect number")
# else:
#     print("is not perfect number")


a = int(input("Enter the number : "))
sum = 0
i = a
while a > 0:
    sum = sum+(a%10)*(a%10)*(a%10)
    a = a // 10
if i == sum:
    print("armstrong")
else:
    print("not armstrong")