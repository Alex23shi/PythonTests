import sys

def DicList():
    YahDic = open('YahooDictationary.txt', 'r')
    list = []
    for line in YahDic.read().splitlines():
        list.append(line)
    return (list)

def PWList():
    PW = open('password.file', 'r', encoding='ISO-8859-1')
    list = []
    for line in PW.read().splitlines():
        list.append(line)
    return (list)


def main():
    a = DicList()  # assigning the value from the wordlist to a
    b = PWList()  # assigning the value from the password dump to b

    for i in range(len(a)):  # traversing the list a
        for j in range(len(b)):  # traversing the list b
            k = b[j].split(':', 2)  # assigning the password value from password dump to c
            if (a[i] in k):  # comparing the passwords from the dump and the wordlist
                sys.stdout = open('CS5615_Yahoo.txt', 'a')
                print(b[j].split(':', 1)[-1], ':', a[i])  # printing the email-id and the password
                sys.stdout.close()
                break  # using break in order to remove the multiple ids with same passwords


if __name__ == '__main__':
    main()
