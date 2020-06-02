import numpy as np
from numpy.linalg import inv
M = np.matrix('1 1 1; 4 2 1; 9 3 1')
Minv = inv(M)
a = np.matrix('1; 3; 13')
b = np.matrix('1; 9; 25')
c = np.matrix('1; 5; 17')
d = np.matrix('1; 7; 21')

x = lambda m : 4*m**2-10*m+7
y = lambda m : 4*m**2-4*m+1
z = lambda m : 4*m**2-8*m +5
zz = lambda m : 4*m**2-6*m+3

b=[]
i = 2
while True:
    b.append(y(i)) 
    if y(i)==1001**2: break
    i+=1

length = i
a = [x(i) for i in range(2,length+1)]
c = [z(i) for i in range(2,length+1)]
d = [zz(i) for i in range(2,length+1)]

print(sum(a+b+c+d)+1)