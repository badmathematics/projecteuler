months = [31, 28,31,30,31,30,31,31,30,31,30,31]
days = [1,2,3,4,5,6,7]

year = 1901
count = 0
a = 0
correction = 0
while year <= 2000:
    
    if year&4 ==0:
        leap = True
    else:
        leap = False    
    for days in months:
        if days == 28 and leap:
            a = a+1+days
            print("here")
        else:
            a = a + days
        if (a+1)%7==0:
            count+=1

    correction = a%7

    year += 1
    
print(count)