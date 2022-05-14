import random
HANGMANPICS = ['''

 +---+
     |
     |
     |
    ---''','''
 +---+
 0   |
     |
     |
    ---''','''
 +---+
 0   |
 |   |
     |
    ---''','''
 +---+
 0   |
/|   |
     |
    ---''','''
 +---+
 0   |
/|\  |
     |
    ---''','''
 +---+
 0   |
/|\  |
/    |
    ---''','''
 +---+
 0   |
/|\  |
/ \   |
    ---''']
words ='скунс баран папуас опосум бык корова козел кошка собака волк воробей гусь голубь' .split()
#1 функция
def RandomWord(wordSpisok):
    wIndex = random.randit(0, len(wordSpisok)-1)
    return wordSpisok[wIndex]
#2 функция
def displayBoard(errorB,yesB,sicretS, prostB):
    print(HANGMANPICS[len(errorB)])
    print()
    print('Ошибочные буквы:',end=' ')
    for letter in errorB:
        print(letter,end=' ')
    print()
    slovo = '_'*len(sicretS)
    for sl in range(len(sicretS)):
        if sicretS[sl] in yesB:
            slovo = slovo[:sl]+sicretS[sl]+slovo[sl+1:] 
    print('Секретное слово:',end=' ')
    for pr in prostB:
        print(pr,end=' ')
    print()
eB = 'клфу'
yB = 'о'
sS = 'ворон'
pB = '_о_о_'
displayBoard(eB,yB,sS,pB)
#проверка 2 функции(3 функция)
def ProverkaVvod (Vvod):
    while True:
        k = int(input('Введите букву'))
        k = k.lower()
        if len(k) !=1:
            print('Введите только одну букву')
        elif k in Vvod:
            print('Введите букву, а не другой символ')
        elif k not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Введите только букву, а не другой символ')
        else:
            return k
#4 функция
def playAgain():
    print('Хотите ли вы сыграть ещё? Да или нет')
    while True:
        otvet = input(). lower()
        if(otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            return True
        elif(otvet == 'нет') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            return False
        else:
            print('''Я вас не понял, напишите пожалуйста да или нет''')



    


      
   

    





    
