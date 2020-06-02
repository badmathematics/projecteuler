import math as math
M = int(input("enter a number: M =  "))
sum = 0
a = str(math.factorial(M))
print("M! = ", a)
for i in a:
    sum = sum + int(i)
print("The sum of the digits of M! is ",sum)