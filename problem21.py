def divisors(n):
    M = []
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            M.append(i)
    return M

A = []
for i in range(1,10000):
    a = divisors(i)
    a = sum(a)
    b  = divisors(a)
    b = sum(b)
    if b == i and i != a:
        A.append([i,a])

sum = 0
for i in A:
    sum = sum + i[0]

print(sum)