from collections import Counter

flag = True
i=1000
while flag:
    num1 = str(i)
    num2 = str(2*i)
    num3 = str(3*i)
    num4 = str(4*i)
    num5 = str(5*i)
    num6 = str(6*i)
    if Counter(num1)-Counter(num2) == {}:
        if Counter(num3) - Counter(num2) == {}:
            if Counter(num4) - Counter(num3) == {}:
                if Counter(num5) - Counter(num4) =={}:
                    if Counter(num6) - Counter(num5) == {}:
                        print(num1, num2, num3)
                        flag = False
    i += 1