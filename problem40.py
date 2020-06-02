
champ = ""
for i in range(1,200000):
    champ = champ + str(i)
print(len(champ))
print(int(champ[0])*int(champ[9])*int(champ[99])*int(champ[999])*int(champ[9999])*int(champ[99999])*int(champ[999999]))