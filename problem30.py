M = 0
i=21
lista =[]
while len(lista) <= 5:
    suma = 0
    
    
    for j in str(i):
        suma = suma+int(j)**5
        
    if suma == i:
        lista.append(i)
        
    i+=1
    
print(sum(lista))
