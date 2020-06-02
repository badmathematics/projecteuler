
from fractions import Fraction
from decimal import Decimal
count = 0
for a in range(1,1000):
    frac = Fraction(1,2)+2
    for i in range(0,a):
        frac = 2 + Fraction(1,frac)

    frac = 1+Fraction(1,frac)
    if len(str(frac.numerator)) > len(str(frac.denominator)): count += 1 

print(count)