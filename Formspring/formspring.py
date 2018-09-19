import hashlib
import sys
    
def DicList():
    FSDic = open('passwords.txt', 'r', encoding='ISO-8859-1' )     #opening the file containing the wordlist
    x = []
    y = []
    z = []
    t = [str(d).zfill(2) for d in range(100)]           #zfill argument is used to create two digit integers, ranging from 00 - 99
    
    for line in FSDic.read().splitlines():
        for i in t:                                     #iterating the salt value ranging from 00 - 99
            Nline = i + line                           #adding salt value at the begining the wordlist
            ShaTwo56 = hashlib.sha256()                   #converting the wordlist to SHA256
            ShaTwo56.update((Nline).encode('utf-8'))
            hex = ShaTwo56.hexdigest()
            z.append(i)                                 #adding the values to a list
            x.append(hex)
            y.append(line)
    return(x,y,z)

def PWList():
    PW = open('formspring.txt','r', encoding='utf-8')
    list=[]
    for line in PW.read().splitlines():
        list.append(line)                                 #assinging the hash value from the password dump to list z
    return(list)

def main():
    x,y,z = DicList()                                    #assigning the value from the wordlist to a,b and d
    t = PWList()                                        #assigning the value from the password dump to c
    for i in range(len(x)):
        for j in range(len(t)):
            if(x[i] == t[j]):                             #comparing the passwords in hash format from the dump and the wordlist
                sys.stdout = open('CS5615_FormSpring.txt','a')
                print(t[j], ':', y[i],':',  'salt =', z[i],)     #printing the hash value along with the actual password and the salt value
                sys.stdout.close()
                break
    
if __name__=='__main__':
    main()