
maxa=0
for i in range(1,100):
    for j in range(1,100):
        num = str(i**j)
        a = 0
        for k in num:
            a = a + int(k)
        if maxa < a:
            maxa = a

print(maxa)    