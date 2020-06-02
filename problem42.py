import numpy as np

def quadraticeq(n):
    a = 1
    b = 1
    c = 2*n
    x1 = (-b+np.sqrt(b**2+4*a*c))/(2*a)        
    x2 = (-b+np.sqrt(b**2+4*a*c))/(2*a)
    return [x1,x2]

def is_triangle(num):
    x1, x2 = quadraticeq(num)
    if x1%1 ==0 and x1>0:
        return True
    elif x2%1 == 0 and x2>0:
        return True
    else:
        return False

filename = "p042_words.txt"
lineList = [line.split(',') for line in open(filename)]
a = lineList[0]
A = []
for i in a:
    i = i[1:]
    i = i[:-1]
    A.append(i)
#A.pop(0)

relate = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
print(relate)
count = 0
for word in A:
    sum = 0
    for i in range(0,len(word)):
        sum = sum + relate[word[i]]
    if is_triangle(sum): count += 1


print(count)
