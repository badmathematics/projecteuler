import numpy as np

total = 0
for n in range(2,10001):
    m = 0
    d = 1
    a = int(np.sqrt(n))
    a0=a
    count = 0
    if n%np.sqrt(n)==0:
        continue

    while True:
        m2 = d * a - m
        d2 = (n-m2**2)/d
        a2 = int((a0+m2)/d2)
        #print(m2,d2,a2)
        if 2 * a0 == a2:
            count+=1
            break
        else:
            m = m2
            a = a2
            d = d2 
            count+=1
    #print(n,count)
    if count%2 != 0:
        total += 1

print(total)
