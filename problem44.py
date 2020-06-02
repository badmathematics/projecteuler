import numpy as np
def pentagonal(n):
    return n*(3*n-1)/2
def quadraticeq(n):
    a = 3
    b = -1
    c = -2*n
    if b**2-4*a*c < 0: return False
    x1 = (-b+np.sqrt(b**2+4*a*c))/(2*a)        
    x2 = (-b+np.sqrt(b**2+4*a*c))/(2*a)
    return [x1,x2]


def is_pentagonal(n):
    """function to check if the number
    is pentagonal number or not"""
    if ((1+(24*n+1)**0.5) / 6)%1 == 0:
        return True
    return False

flag = True
i=1
while flag:
    for j in range(1,i):
        add = pentagonal(i)+pentagonal(j)
        diff = pentagonal(i) - pentagonal(j)
        if is_pentagonal(add) and is_pentagonal(diff): 
            
            print(diff)
            flag = False
            break
    i+=1