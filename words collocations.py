import random
import csv
with open('file.csv', 'r', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    d={}
    m=[]
    for key in reader:
        d[key[0]]= key[1:]
        print (d)
    for slovo in d:
        m.append(slovo)
        slovonovo=random.choice(m)
    for slovo in d:
        if slovonovo == slovo:
             phrase=random.choice(d[slovo])
    print('.......', phrase)
    while True :
        requirement = str(input('Введите слово, которое, по вашему мнению, наиболее часто встречается с данным словосочетанием\n Пиши "сдаюсь", если не знаешь, что за слово!\n'))
        requirement = requirement.lower()
        if requirement == slovonovo:
            win=['вы восхитительны!', 'Пожалуй, вы мастер своего дела!', 'Как пить дать!', 'Ух-ты Пух-ты!', 'Поздравляю! Но в следующий раз я придумаю что-нибудь посложнее']
            w=random.choice(win)
            print(w)
        if requirement != slovonovo  and requirement != '':
            lose = ['Ну, ну, попробуй еще раз!', 'Почти... Подумай еще немножко','Ты уверен?' ]
            l=random.choice(lose)
            print(l)
        if requirement == 'сдаюсь':
            print(slovonovo)
