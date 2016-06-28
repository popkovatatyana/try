import re
def opening(path):
    file=open(path, 'r', encoding='utf-8')
    f=file.readlines()
    file.close
    return f
def finding(massiv):
    m=[]
    for string in massiv:
        res=re.search('.*[a-zA-Z].*', string)
        if res:
            m.append(string)
    for el in m:
        if 'LAPP Executive Education 1 Jun 2016' in el:
            m.remove(el) 
    m=('').join(m)
    return m
def writing(final):
    file=open('gonkong.tsv', 'w', encoding='utf-8')
    file.write(final)
    file.close
def main():
    main=writing(finding(opening('gon.txt')))
main()
         
         
