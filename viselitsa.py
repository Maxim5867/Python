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
            print('Введите только одну цифру')
        elif otv not in '1234':
            print('Введите "1", "2", "3" или "4"')
        else:
            return otv
#2 функция

def StavkaHorse():
    print('У вас есть 1000 рублей')
    print('Минимальная ставка 250 рублей')
    print('Напишите сколько денег вы хотите поставить')
    while True:
          stavka = input()
          if stavka not in '1234567890'
              print('Введите любое число от 250 до 1000')
          elif stavka <250:
              print('Введите число больше 250')
          else:
              return stavka
#проверка 2 функции(3 функция)
def ProverkaWin():
    while True:
          wins = input()
          if HoRseVibor != RandomHorse:
              print('Вы проиграли')
          elif HoRseVibor == RandomHorse:
              print('Вы выиграли') 
          else:
              return wins        
def ProverkaSummi(Vvod):
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



