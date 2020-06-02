for i in range(1,1001):
    for j in range(i,1001):
        if 2000*(i+j)-2*i*j == 1000**2:
            a = i
            b = j
            c = 1000-a-b

print(a,b,c)
print(a*b*c)