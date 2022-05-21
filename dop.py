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
/ \  |
    ---''','''
 +---+
[0   |
/|\  |
/ \  |
    ---''','''
+---+
[0]  |
/|\  |
/ \  |
    ---''','''
+---+
[0]- |
/|\  |
/ \  |
    ---''','''
+---+
[0]- |
/|\- |
/ \  |
    ---''']
def LevelVibor(LVL):
    print('Выберите уровень сложности')
    print('Введите l для легкого')
    print('Введите s для среднего')
    print('Введите t для тяжелого')
    while True:
        otv = input().upper()
        if len(otv) !=1:
            print('Введите только одну букву')
        elif otv in LVL:
            print('Введите букву, а не другой символ')
        elif otv not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Введите только букву, а не другой символ')
        else:
            return otv
            
