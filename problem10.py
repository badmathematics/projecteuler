def isprimes(x):
    x = abs(int(x))
    if x < 2:
        return False
    elif x ==2:
        return True
    elif x%2 == 0:
        return False
    else:
        i = 3
        max = x**0.5+1
        while i<=max:
            if x%i == 0:
                return False
            i+=2
    return True

      
def nprime(n):
    if n ==1:
        return 2
    j = 3
    count = 1
    while True:
        if isprime(j):
            count = count+1

        if count == n:
            break
        j=j+2
    return j

M = int(input("Find sum of all primes below M = "))



sum = 0
for j in range(2,M):
 if isprimes(j):
    sum = sum+j

print("sum is ", sum)