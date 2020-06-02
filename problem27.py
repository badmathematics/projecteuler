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

Bs = []
for i in range(0,1001):
    if isprimes(i):
        Bs.append(i)
        #if i != 0: Bs.append(-i)

As = []
for i in range(0,1001):
    As.append(i)
    if i != 0: As.append(-i)


maxlen = 0
besta = 0
bestb = 0
for b in Bs:
    
    for a in As:
        length = 0    
        sequence = []
        while isprimes(length**2+a*length+b):
            sequence.append(length**2+a*length+b)
            length += 1
        
        newlen=len(sequence)
        if newlen > maxlen: 
            maxlen = newlen
            besta = a
            bestb = b
            maxsequence = sequence

print(maxlen, besta, bestb)
print(maxsequence)
print(len(maxsequence))
print("product is ab =  ", besta*bestb)


