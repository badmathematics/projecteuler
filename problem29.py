M = 100

b = [4]
for i in range(2,M+1):
    a = []
    for j in range(2,M+1):
        a.append(i**j)
    
    for k in a:
        flag = True
        for kk in b:
            if kk == k:
                flag = False
        if flag: b.append(k)


 
print(len(b))
