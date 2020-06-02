fn = 1
fn1 = 1

def digits(n):
    i = 0
    for a in str(n):
        i+=1
    return i
i = 2
while digits(fn1) < 1000:
    fn2 = fn1 + fn
    fn = fn1
    fn1 = fn2
    i+=1
    print(i, fn1, digits(fn1))


print("index = ",i)
