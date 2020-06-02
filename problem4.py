store = []
for i in range(100,999):
    for j in range(100,999):
        num = str(i*j).split()[0]
        if len(num) == 6:
            if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
                store.append(j*i)

print(max(store))