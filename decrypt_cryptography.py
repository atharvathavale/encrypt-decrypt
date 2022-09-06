import numpy as np
import re

encrypt = np.array([[0, 2, -1], [1, -2, 1], [1, -1, 1]])
print(encrypt)

key = dict()
key = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15,\
       'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, ' ':27}

def get_key(val):
    for keys, value in key.items():
         if val == value:
             return keys

def decryptmessage(encrypted):

    decrypt = np.linalg.inv(encrypt)
    print(decrypt)
    decrypted = []
    count = 0
    for i in range(len(encrypted)):
        count = count + 1
        if(count % 3 == 0):
            small = np.array([[encrypted[i-2]], [encrypted[i-1]], [encrypted[i]]])
            #print(small)
            C = decrypt.dot(small)
            for i in range(0, 3):
                #print(C[i], end = ' ')
                decrypted.append(int(C[i]))
    print(decrypted)
    print('Decrypted Message: ', end = '')
    for i in decrypted:
        if(int(i) != 0):
            print(get_key(int(i)), end = '')
    return decrypted

if __name__ == "__main__":
    fp = open("encryptsecret.txt", "r")
    fp2 = open("decryptedsecret.txt", "w")
    line = fp.readline()
    while line:
        line1 = []
        line = re.split(', |\n|\[|\]', line)
        while('' in line):
            line.remove('')
        for i in line:
            line1.append(int(i))
        decrypted = decryptmessage(line1)
        for i in decrypted:
            if(int(i) != 0):
                print(get_key(int(i)), end = '', file = fp2)
        print('', file = fp2)
        line = fp.readline()
    fp.close()
    fp2.close()
