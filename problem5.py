flag = True
i = 20
num = [k for k in range(1,i+1)]
while flag:
    for k in num:
        if i%k !=0:
            flag = True
            break
        flag = False
    if flag == True:
        i = i + 10
print(i)