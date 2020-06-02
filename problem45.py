from numpy import sqrt
def is_pentagonal(n):
    """function to check if the number
    is pentagonal number or not"""
    if ((1+(24*n+1)**0.5) / 6)%1 == 0:
        return True
    return False

def is_hexagonal(n):
    if ((sqrt(8*n+1)+1)/4) %1 == 0:
        return True
    return False

flag = True
i = 286
while flag:
    T = i*(i+1)/2
    if is_hexagonal(T) and is_pentagonal(T):
        print(T)
        flag = False
    i+=1