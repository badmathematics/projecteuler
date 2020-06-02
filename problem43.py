from itertools import permutations
p = permutations('0123456789')

count = 0
for i in p:
    if i[0]=='0':
         continue
    elif (int(''.join(i[7:10]))%17 ==0 and
        int(''.join(i[6:9]))%13 ==0  and
        int(''.join(i[5:8]))%11 ==0  and
        int(''.join(i[4:7]))%7 ==0  and
        int(''.join(i[3:6]))%5 ==0  and
        int(''.join(i[2:5]))%3 ==0  and
        int(''.join(i[1:4]))%2 ==0):
        count += int(''.join(i))

print(count)