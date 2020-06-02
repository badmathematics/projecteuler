import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

count = 0

for i in range(1,101):
    for j in range(1,101):
        if ncr(i,j) > 1000000:
            count += 1

print(count)