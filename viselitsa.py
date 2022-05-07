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
def playAgain(play):
    print('Хотите ли вы сыграть ещё? Да или нет')
    return input(). lower()
#2 функция
def displayBoard(missedLetters,correctLetters,secretLetters):
 print(HANGMANPICS(len(missedLetters)))
 print()
 blanks = '_' ' len(secretword)
 for i in range(len(secretword)):
  if secretWord(i) incorrectLetters:
   blanks = blanks(:i) + secretWord(i) + blanks(i+i:)
 for letter in blanks:
   print(letter,end=' ')
 print()
      
   

    





    
