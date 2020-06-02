# #Project Euler Problem 59
# from collections import Counter

# encoded_text = map(int, open('cipher.txt').read().split(','))
# print(encoded_text)
# key = [Counter(encoded_text[i::3]).most_common(1)[0][0] ^ 32 for i in range(3)]
# print('Encryption key =', ''.join(map(chr, key)))
# print( 'Sum of ASCII values in decrypted text') 
# print( sum(x^y for x, y in zip(encoded_text, key*(len(encoded_text)//3+1))))

from math import ceil
import string

def test():
    asciis = open('cipher.txt', 'r').read()
    encCodes = [int(s) for s in asciis.split(',')]

    asciiSum = 0
    
    pKeys = plausibleKeys(encCodes, 3)
    for k0 in pKeys[0]:
        for k1 in pKeys[1]:
            for k2 in pKeys[2]:
                text = "".join(applyKey([k0,k1,k2], encCodes))
                if(properStringProbability(text)):
                    print(text)
                    asciiSum = sum([ord(c) for c in text])
    return asciiSum

def plausibleKeys(encCodes, keyLen):
    pKeys = {
        0: [x for x in range(255)],
        1: [y for y in range(255)],
        2: [z for z in range(255)]
        }

    for i, c in enumerate(encCodes):
        for k in pKeys[i % keyLen]:
            if chr(c ^ k) not in string.printable:
                pKeys[i % keyLen].remove(k)

    print(pKeys)
    return pKeys

def properStringProbability(string):
    cnt = 0
    for word in ["the", "and", "have", "that", "you"]:
        cnt += string.count(word)        
    return cnt > 5


def applyKey(key, asciiText):
    return [chr(x ^ int(y)) for (x,y) in zip(key * int(ceil(len(asciiText) / 3)),asciiText)]




print(test())