from numpy import sqrt
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

FLAG = True
i = 33
while FLAG:
    if isprimes(i):
        i+=2
        continue
    else:
        flag = False
        for j in range(1,int(sqrt(i/2))+2):
            if isprimes(i-2*j**2): flag = True
        if not flag:
            FLAG = False
            print(i)
    # print(i)
    i+=2
        