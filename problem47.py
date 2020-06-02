import math
# A function to print all prime factors of  
# a given number n 
def primeFactors(n): 
    flag = True
    A = set()
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        A.add(2)
        #print( 2) 
        n = n / 2
        flag = True
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            A.add(i) 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        A.add(n)
    return A 

flag = True
i = 20
j = 21
k = 22
l = 23
count = 0
ilen = len(primeFactors(i))
jlen = len(primeFactors(j))
klen = len(primeFactors(k))
llen = len(primeFactors(l))
while flag:
    
    if ilen == 4 and jlen == 4 and klen == 4 and llen==4:
        print(i,j,k,l)
        flag = False
    
    i = j
    j = k
    k = l
    l += 1
    ilen = jlen
    jlen = klen
    klen = llen
    llen = len(primeFactors(l))  
    
    