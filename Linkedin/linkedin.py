import hashlib
import sys

def DicList():
    LinDic = open('passwords.txt', 'r', encoding='ISO-8859-1')
    x = []
    y = []
    for line in LinDic.read().splitlines():
        ShaOne = hashlib.sha1()
        ShaOne.update((line).encode('utf-8'))
        hex = ShaOne.hexdigest()
        hex = '00000' + hex[5:].strip() #add 00000, some of the encrypted lines have the 00000 pattern, so I did the same to the dictionary
        x.append(hex)
        y.append(line)
    return (x, y)

def PWList():
    PW = open('SHA1.txt', 'r', encoding='utf-8')
    list = []
    for line in PW.read().splitlines():
        list.append(line)
    return (list)

def main():
    x, y = DicList()
    z = PWList()
    for i in range(len(x)):
        for j in range(len(z)):
            if (x[i] == z[j]): #compare if the lines are identical
                sys.stdout = open('CS5615_LinkedIN.txt', 'a')
                print(z[j], ':', y[i])
                sys.stdout.close()
                break

if __name__ == '__main__':
    main()
