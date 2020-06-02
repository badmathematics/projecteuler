import numpy as np

def get_c(a,b):
    return np.sqrt(a**2+b**2)
max = 0
maxp = 0
for p in range(1,1000):
    count = 0
    for a in range(1,p):
        for b in range(a,p):
            c = get_c(a,b)
            if c%1 == 0:
                if a+b+c == p:
                    print(a,b,c,p,max,maxp)
                    count += 1
    if max < count:
        max = count
        maxp = p

print(max,maxp)
