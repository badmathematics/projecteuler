
import math as math
def divisor(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            number_of_factors +=2
        if i*i==n:
            number_of_factors -=1
    return number_of_factors

num = 0 
M = 500
i = 2
sum = 3
while num < M:
    i = i+1    
    sum = sum + i
    a = divisor(sum)
    if a> num:
        num = a
   

print(sum)
