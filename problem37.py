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
count = 1
i = 11
primes = []
sum = 0
while count <= 11:

    if isprimes(i):
        a = str(i)
        b = []
        k = ""
        if isprimes(int(a[0])):
            for j in a:
                k = k + j
                b.append(int(k))
            for j in range(0,len(a)-1):
                b.append(int(a[1:]))
                a = a[1:]
            #print(b)    
            
            flag = True
            for num in b:
                if not isprimes(num):
                    flag = False
                    break
            if flag == True:
                count+=1
                primes.append(i)
                print(count, i)
                sum += i
    i+=1
    
print(count)
print(primes)
print("sum = ",sum)