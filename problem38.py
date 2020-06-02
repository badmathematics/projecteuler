def is_pandigital(n, s=9): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)

def concate_product(num,n):
    n = [i for i in range(1,n+1)]
    concat = ""
    for i in n:
        concat = concat + str(num*i)
    
    return int(concat)

for i in range(1,10000):
    for j in range(2,100):
        a = concate_product(i,j)
        if is_pandigital(a):
            print(a)

