from itertools import combinations, permutations

def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

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

def comb(a,b):
    num1 = int(str(a)+str(b))
    num2 = int(str(b)+str(a))
    if (isprimes(num1) and isprimes(num2)):
        return True
    return False

primes = sieve(10000)


for a in primes:
    for b in primes:
        if b < a:
            continue
        if comb(a,b):
            for c in primes:
                if c < b:
                    continue
                if comb(a,c) and comb(b,c):
                    for d in primes:
                        if d < c:
                            continue
                        if comb(a,d) and comb(b,d) and comb(c,d):
                            for e in primes:
                                if e < d:
                                    continue
                                if comb(a,e) and comb(b,e) and comb(c,e) and comb(d,e):
                                    print(a,b,c,d,e)
                                    print(a+b+c+d+e)