N = 1000
sum = 0
for i in range(1,N+1):
    sum += i**i
sum = str(sum)
print(sum[-10:])
