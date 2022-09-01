import random
def sozdaniehorse():
    HORSES = ['''
 [Первая]
 [Вторая]
 [Третья]
 [Четвертая]''','''
       [Первая]
      [Вторая]
            [Третья]
     [Четвёртая]''','''
                      [Первая]
                [Вторая]
                             [Третья]
                      [Четвертая]''','''
                                    [Первая]
                                   [Вторая]  
                                                   [Третья] ФИНИШ!
                                              [Четвёртая]''' 
                                                                                                                               

    return HORSES

horse = {'лошади' 'первая', 'вторая', 'третья','четвертая' .split()}
#1 функция
def RandomHorse(HOrseSpisok,hore):
    if hore == '1':
        for i in range(len(list(HOrseSpisok .keys()))):        #range(len(list(HOrseSpisok.keys()))):
            print('Введите '+str(i)+' для '+list(HOrseSpisok.keys())[i])
        vybK = input()
        vybK = int(vybK)
        wordKey = list(HOrseSpisok.keys())[vybK]
    else:    
        wordKey = random.choice(list(HOrseSpisok.keys())) 
    wIndex = random.randint(0, len(HOrseSpisok)[wordKey])-1)
    return [HOrseSpisok[wordKey][wIndex],wordKey]

def HoRseVibor():
    print('Выберите номер лошади')
    print('Введите "1" для первой')
    print('Введите "2" для второй')
    print('Введите "3" для третьей')
    print('Введите "4" для четвёртой')
    while True:
        otv = input().upper()
        if len(otv) !=1:
            print('Введите только одну букву')
        elif otv not in 'LST':
            print('Введите "1", "2", "3" или "4"')
        else:
            return otv
#2 функция
def displayBoard(errorB,yesB,sicretS,hangP):
    print(hangP[len(errorB)])
    print()
    print('Ошибочные буквы:',end=' ')
    for letter in errorB:
        print(letter,end=' ')
    print()
    slovo = '_'*len(sicretS)
    for sl in range(len(sicretS)):
        if sicretS[sl] in yesB:
            slovo = slovo[:sl]+sicretS[sl]+slovo[sl+1:]

    for ls in slovo:
        print(ls, end=' ')
    print() 

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



delV = True
errorB = ''
yesB = ''
gameOver = False
while True:
    if delV:
        hm = sozdanieVis()     
        bS = LevelVibor()
        deletVis(bS,hm)
        sicretS,keyWords = RandomWord(words,bS)
        delV = False
    if bS == 'L':
        print('Категория слова: '+keyWords)
    displayBoard(errorB,yesB,sicretS,hm)
    bukva = ProverkaVvod(errorB+yesB)
    if bukva in sicretS:
        yesB = yesB + bukva
        ssYes = True
        for i in range(len(sicretS)):
            if sicretS[i] not in yesB:
                ssYes = False
                break
        if ssYes:
            displayBoard(errorB,yesB,sicretS,hm)
            print('Вы выиграли. Вы отгадали слово за '+str(len(yesB+errorB))+' количество ходов')
            gameOver = True
    else:
        errorB = errorB + bukva
        if len(errorB) 
