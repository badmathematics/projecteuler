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

x = lambda m : 4*m**2-10*m+7
y = lambda m : 4*m**2-4*m+1
z = lambda m : 4*m**2-8*m +5
w = lambda m : 4*m**2-6*m+3

a = [x(i) for i in range(1,5)]
b = [y(i) for i in range(1,5)]
c = [z(i) for i in range(1,5)]
d = [w(i) for i in range(1,5)]

P=[]
np=[1]
flag = True
i = 2
while flag:
    a = x(i)
    b = z(i)
    c = w(i)
    np.append(y(i))
    if isprimes(a):
        P.append(a)
    else:
        np.append(a)
    if isprimes(b):
        P.append(b)
    else:
        np.append(b)
    if isprimes(c):
        P.append(c)
    else:
        np.append(c)
    #print(len(P)/(len(P)+len(np)),i)
    if len(P)/(len(P)+len(np))<.1: 
        flag = False
    else:
        i += 1
print(2*i-1)

    
     