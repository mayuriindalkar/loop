k=9 
i=1
while(i<=5):
    j=1
    while(j<=i):
        print(" ",end=" ")
        j=j+1 
    t=1 
    while(t<=k):
        print("*",end=" ")
        t=t+1  
    k=k-2 
    print()
    i=i+1


# row=0
# while row<6:
#     column=0
#     while column<7:
#         if (row==0 and column%3!=0) or (row==1 and column%3==0) or (row-column==2) or (row+column==8):
#             print("m",end=" ")
#         else:
#             print(end=" ")
#         column=column+1
#     print()
#     row=row+1

# i=1
# while i<=20:
#     print(i)
#     i-=-1 

# num=int(input("enter the number : "))
# i=0
# while i<=num:
#     print("*"*i,end=" ")
#     i=i+1
#     print()

# num=int(input("enter the number : "))
# i=0
# while i<=num:
#     i=i+1
#     print("*",end=" ")
#     print()