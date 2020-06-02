

def reverse(s):
    s = str(s)
    sol = ''
    for i in s:
        sol = i + sol
    return int(sol)

def palindromes(num):
    s = str(num)
    sol = ''
    for i in s:
        sol = i + sol
    return int(sol) == num

count = 0
for i in range(10,10000):
    num = i + reverse(i)
    
    for j in range(2,51):
           
        if not palindromes(num): 
            num = num+reverse(num)        
        else:
            break
    print(count)
    if j == 50:
        count += 1
        
print(count)