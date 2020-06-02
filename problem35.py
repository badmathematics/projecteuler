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

count = 0
for num in range(2,1000001):
    if isprimes(num):
        num = str(num)
        j = 0
        for i in num:
            num = num[1:]+num[0]
            if not isprimes(int(num)):
                break
            j+=1
        if j == len(num):
            count+=1

print(count)