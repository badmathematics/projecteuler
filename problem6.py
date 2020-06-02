def isprime(a):
    if a < 0:
        return False
    if a == 2:
        return True
    
    for x in range(3, int(a**0.5)+1, 2):
        if a % x == 0:
            return False
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


print(nprime(10001))    