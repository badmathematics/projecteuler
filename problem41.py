def is_pandigital(n, s=9): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)
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
for n in range(8,10):

    for i in range(10**(n-1),10**n):
        if is_pandigital(i,n): 
            if isprimes(i):
                print(i)