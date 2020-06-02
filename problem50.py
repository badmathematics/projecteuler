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

primes=[2]
for i in range(2,1000000):
    if i%2==0:
        continue
    elif isprimes(i):
        primes.append(i)

print(len(primes))
#print(primes)

count = 1
position = 2
maxcount = 0

lastj = len(primes)
leng = 0
flag = False

for i in range(0,len(primes)):
    for j in range(i+leng,lastj):
        sol = sum(primes[i:j])
        if sol < 1000000:

            if sol in primes:
                length = j-i
                if leng < length:
                    leng = length
                    num = sol
        else:
            lastj = j+1
            break

print(leng, num)