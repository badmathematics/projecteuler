def divisors(n):
    M = []
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            M.append(i)
    return M

def isAbundant(n):
    a = sum(divisors(n))
    if a > n:
        return True
    else:
        return False

abundant = []
for i in range(12,28123):
    if isAbundant(i):
        abundant.append(i)

not_abundant=[i for i in range(1,28124)]
print(len(not_abundant))
for i in range(0,len(abundant)):
    for j in range(i,len(abundant)):
        if (abundant[i]+abundant[j]<28123):
            #print(i,j, abundant[i]+abundant[j])
            not_abundant[abundant[i]+abundant[j]]=0
        else:
            break

print(sum(not_abundant))