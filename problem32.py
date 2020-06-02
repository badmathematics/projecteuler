def is_pandigital(n, s=9): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)

def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates '''    
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False
store = set()
for i in range(1,10000):
    
    if checkIfDuplicates_2(str(i)):
        flg = True
    else:
        
        for j in range(1,10000):
            if checkIfDuplicates_2(str(i)+str(j)):
                flg = True
            else:
                k = i * j
                if checkIfDuplicates_2(str(i)+str(j)+str(k)):
                    flg = True
                else:
                    if is_pandigital(str(i)+str(j)+str(k)):
                        store.add(k)    
                        print(i,j,k)

print(store)
print(sum(store))        