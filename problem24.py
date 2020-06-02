from itertools import permutations

perm = permutations([i for i in range(0,10)])

j = 0
M = []
for i in list(perm):
    a=""
    for k in i:
        a = a+str(k)
    M.append(int(a))

M = sorted(M)
#print(M[999998])
print(M[999999])
#print(M[1000000])