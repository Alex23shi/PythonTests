import hashlib
import sys
    
def DicList():
    FSDic = open('passwords.txt', 'r', encoding='ISO-8859-1' )
    x = []
    y = []
    z = []
    t = [str(d).zfill(2) for d in range(100)]           #create the salt
    for line in FSDic.read().splitlines():
        for i in t:
            Nline = line + i                           #add salt value, tried originally at the end of each line, but no result returned, so tried add salt at the beginning of each line
            ShaTwo56 = hashlib.sha256()
            ShaTwo56.update((Nline).encode('utf-8'))
            hex = ShaTwo56.hexdigest()
            z.append(i)
            x.append(hex)
            y.append(line)
    return(x,y,z)

def PWList():
    PW = open('formspring.txt','r', encoding='utf-8')
    list=[]
    for line in PW.read().splitlines():
        list.append(line)
    return(list)

def main():
    x,y,z = DicList()
    t = PWList()
    for i in range(len(x)):
        for j in range(len(t)):
            if(x[i] == t[j]):                             #compare the lines as usual...
                sys.stdout = open('CS5615_FormSpring.txt','a')
                print(t[j], ':', y[i])
                sys.stdout.close()
                break
    
if __name__=='__main__':
    main()