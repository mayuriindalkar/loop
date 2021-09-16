# i=0
# while i<=10:
#     if i==8:
#         break
#     i=i+1
#     print(i)


# num=int(input("enter the row number : "))
# row=0
# while row<num:
#     space=num-row-1
#     star=row+1
#     while star>0:
#         print("*",end=" ")
#         star=star-1
#     row=row+1
#     print()

# num=int(input("enter the row number : "))
# row=0
# while row<num:
#     space=num-row-1
#     star=row+1
#     while star>0:
#         print("#",end=" ")
#         star=star-1
#     row=row+1
#     print()


# n=int(input("enter the row number : "))
# i=1
# while n>0:
#     b=1
#     while b<i:
#         print("*",end=" ")
#         b=b+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     n=n-1
#     i=i+1



# num=int(input("enter the row number : "))
# row=0
# while row<num:
#     space=num-row-1
#     star=row+1
#     while star>0:
#         print(star,end=" ")
#         star=star-1
#     row=row+1
#     print()

# num=int(input("enter the row number : "))
# row=0
# while row<num:
#     space=num-row-1
#     while space>0:
#         print(end=" ")
#         space=space-1
#     star=row+1
#     while star>0:
#         print(star,end=" ")
#         star=star-1
#     row=row+1
#     print()


# for row in range(5):
#     for col in range(5):
#         if ((col==row)) or ((col+row==4)):
#             print(col,end='')
#         else:
#             print(end=' ')
#     print()


# num=int(input("enter the number : "))
# i=0
# while i<num:
#     space=num-i-1
#     while space>0:
#         print(end=" ")
#         space=space-1
#     star=i+1
#     while star>0:
#         print("*",end=" ")
#         star=star-1
#     i=i+1
#     print()



# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1

# num=int(input("enter the number of rows : "))
# i=0
# while i<num:
#     i=i+1
#     print("$"*i)

# num=int(input("enter the number : "))
# i=0
# while i<num:
#     i=i+1
#     print(" "*(num-i)+"*"*i)

# num=int(input("enter the number row : "))
# i=0
# while i<num:
#     j=num+1
#     i=i+1
#     print(" "*(num-i)+"*"*i)

num=int(input("enter the row number : "))
i=0
while i<num:
    i=i+1
    print(" "*(num-i)+"* "*i)
    while i>num:
        i=i-1
        print(" "*(num-i)-"* "*i)
    print()


# num=int(input("enter the row number : "))
# for i in range (num,0,-1):
#     print(" "*(num-i)+"* "*i)


# num=int(input("enter the number : "))
# i=0
# while i<num:
#     i=i+1
#     print(" "*(num-i)+"* "*i)
    # while i>num:
    #     i=i-1
    #     print(" "*(num-i)-"* "*i)
    # print()
    

# num=int(input("enter thr row number : "))
# i=0
# while i<num:
#     i=i+1
#     print(" "*(num-i)+"*"*i)
#     print()