def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numer, denom):

    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if reduced_den == 1:
        return "%d/%d is simplified to %d" % (numer, denom, reduced_num)
    elif common_divisor == 1:
        return "%d/%d is already at its most simplified state" % (numer, denom)
    else:
        return "%d/%d is simplified to %d/%d" % (numer, denom, reduced_num, reduced_den)

nprod = 1
dprod = 1
store = []
for n in range(11,99):
    if n%10 == 0: continue
    for d in range(n+1,99):
        
        flag = False
        for i in range(0,2):
            for j in range(0,2):
                if str(n)[i] == str(d)[j]:
                    flag = True 
                    remove = str(n)[i]
                    
        if flag:
            
            n2 = ''
            t = False
            for i in str(n):
             if i != remove or t:
                n2 = n2 + i
             else:
                t = True
            d2 = ''
            t = False
            for i in str(d):
                if i != remove or t:
                    d2 = d2 + i
                else:
                    t = True
            if int(d2)== 0: continue
            print(n,d,n2,d2, n/d, int(n2)/int(d2))
       
            if int(n2)/int(d2) == n/d:
                nprod = int(n2)*nprod
                dprod = int(d2)*dprod
                store.append((n,d,n2,d2))

        
print(simplify_fraction(nprod,dprod))
print(store)