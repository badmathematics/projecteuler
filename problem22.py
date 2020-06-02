
f=open("p022_names.txt",'r')
char_num_dict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
names=sorted(f.read().replace('"','').split(','),key=str)
sum=0

i =1
for name in names:
    for letter in name:
        sum+=char_num_dict[letter]*i
    i=i+1
print(sum)