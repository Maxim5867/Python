from dis import dis
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
    wIndex = random.randint(0, len(wordSpisok)-1)
    return wordSpisok[wIndex]
#2 функция
def displayBoard(errorB,yesB,sicretS):
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
#проверка 2 функции(3 функция)
def ProverkaVvod(Vvod):
    while True:
        Vvo = input('Введите букву')
        Vvo = Vvo.lower()
        if len(Vvo)!=1:
            print('Введите только одну букву')
        elif Vvo in Vvod:
            print('Введите букву, а не другой символ')
        elif Vvo not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Введите только букву, а не другой символ')
        else:
            return Vvo
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

errorB = ''
yesB = ''
sicretS = RandomWord(words)
print(sicretS)
gameOver = False
while True:
    displayBoard(errorB, yesB,sicretS)

    bukva = ProverkaVvod(errorB+yesB)
    if bukva in yesB:
        yesB = yesB + bukva
        ssYes = True
        for i in range(len(sicretS)):
            if sicretS[i] not in yesB:
                ssYes = False
                break
        if ssYes:
            displayBoard(errorB,yesB,sicretS)
            print('Вы выиграли. Вы отгадали слово за '+str(len(yesB+errorB))+' количество ходов')
            gameOver = True
    else:
        errorB = errorB + bukva
        if len(errorB) == len(HANGMANPICS) -1:
            displayBoard(errorB,yesB,sicretS)
            print('Вы проиграли. Секретное слово: '+sicretS)
            gameOver = True
            
    if gameOver:
        if playAgain():
            errorB = ''
            yesB = ''
            sicretS = RandomWord(words)
            gameOver = False
        else:
            break

        

    

