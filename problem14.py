maxlen = 0
start = 1
savenum = 1
for i in range(1,1000000):
    length = 0
    start = i
    while i != 1:
        if i%2 == 0:
            i = i/2
        else:
            i = 3*i+1
        length += 1
        if length > maxlen:
            maxlen=length
            savenum = start
print(savenum, maxlen)