def shifr():
    string=input('введите строку: ')
    n=0
    k=0
    i=0
    a1='абвгдеёжзийклмнопрстуфкцчшщыъьэюяа \n'
    alf=list(a1)
    m1=list(string)
    for letter in m1:
            while m1[i] != alf[n]:
                    n+=1
            print(alf[n+1], end='')
            n=0
            i+=1
            
def opening(path):
    file = open(path,'r', encoding = 'utf-8') 
    f = file.readlines()
    file.close()
    return f

def cleaning(massiv):
    mnew=[]
    for string in massiv:
        words = string.split(' ')
        for word in words:
            word1 = word.lower()
            word2 = word1.strip('!@$%^&*()_+,./[]{}<>~`\n\t ')
            mnew.append(word2)
    #result = ', '.join(mnew)
    return mnew

def frequency (massiv):
    d={}
    for word in massiv:
             if word in d:
                d[word]+=1
             else:
                d[word]=1
    for key in sorted(d, key =d.get, reverse= True):
        st=''
        st+=key + ': ' + str(d[key])+'\n'
        return st
        
def writing (text):
    file = open('nameoffile.tsv', 'w', encoding='utf-8')
    file.write(text)
    file.close

def searching (massiv):
    #import re
    m=[]
    for string in massiv:
        res= re.search(regex, string)
        if res:
            m.append(string)
    m=''.join(m)
    return m

#(.[^ ]*?(?:ыя|ія) (?:.*? ))
            


