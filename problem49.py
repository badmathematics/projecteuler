from itertools import permutations
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

def create(b):
    for i in range(0,len(b)):
        for j in range(i+1, len(b)):
            difference = b[j] - b[i]
            if b[j] + difference in b:
                return str(b[i])+str(b[j])+str(b[j]+difference)
    return False

M = 10000
for i in range(1000,M+1):
    if isprimes(i):
        p = list(permutations(str(i)))
        #p = [int(j) for j in p]
        
        P =[]
        for a in p:
            join = ""
            for b in a:
                join = join + b
            if int(join) > 1000:
                P.append(int(join))
        
        A = set()
        for j in P:
            if isprimes(j):
                A.add(j)
        A = list(A)
        A.sort()
        
        if len(A)>=3:
            if create(A):
                print(create(A))