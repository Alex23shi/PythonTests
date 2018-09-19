import sys

def DicList():
    YahDic = open('passwords.txt', 'r',encoding='ISO-8859-1')
    list = []
    for line in YahDic.read().splitlines():
        list.append(line)
    return (list)

def PWList():
    PW = open('password.file', 'r',encoding='ISO-8859-1')
    list = []
    for line in PW.read().splitlines():
        list.append(line)
    return (list)


def main():
    d = DicList()
    p = PWList()

    for i in range(len(d)):
        for j in range(len(p)):
            k = p[j].split(':', 2)
            if (d[i] in k):
                sys.stdout=open('CS5615_Yahoo.txt', 'a')
                print(p[j].split(':', 1)[-1], ':', d[i])
                sys.stdout.close()
                break


if __name__ == '__main__':
    main()
