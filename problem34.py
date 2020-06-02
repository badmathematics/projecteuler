from math import factorial
total = 0
for i in range(3,10000000):
    digits = []
    for num in str(i):
        
        digits.append(int(num))
    
    sum = 0
    for j in digits:
        sum += factorial(j)
    #print(i, digits, sum)
    if i == sum:
        total += sum
print(total)