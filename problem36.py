sum = 0
for i in range(1,1000001,2):
    bflag = False
    dflag = False

    bi = "{0:b}".format(i)
    ib = ""
    for j in bi:
        ib = j+ib 
    if ib == bi:
        bflag = True
    
    di = str(i)
    i_d = ""
    for j in di:
        i_d = j + i_d
    if i_d == di:
        dflag = True 
    
    if bflag and dflag:
        sum += i

print(sum)