# def isprimes(x):
#     x = abs(int(x))
#     if x < 2:
#         return False
#     elif x ==2:
#         return True
#     elif x%2 == 0:
#         return False
#     else:
#         i = 3
#         max = x**0.5+1
#         while i<=max:
#             if x%i == 0:
#                 return False
#             i+=2
#     return True

# M = int(input("enter number to find prime factors"))

# store=[]
# for i in range(2,int(M/2)+1):
#     if isprimes(i):
#         if M%i==0:
#             store.append(i)
# print(store)

n=int(input("Enter an integer:"))
print("Factors are:")
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1