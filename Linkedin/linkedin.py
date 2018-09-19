import hashlib
import sys

def DicList():
    LinDic = open('passwords.txt', 'r', encoding='ISO-8859-1')
    x = []
    y = []
    z = '00000'
    for line in LinDic.read().splitlines():
        ShaOne = hashlib.sha1()
        ShaOne.update((line).encode('utf-8'))
        i = ShaOne.hexdigest()
        i = z + i[
                5:].strip()
        x.append(i)
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
            if (x[i] == z[j]):
                sys.stdout = open('CS5615_LinkedIN.txt', 'a')
                print(z[j], ':', y[i])
                sys.stdout.close()
                break

if __name__ == '__main__':
    main()
