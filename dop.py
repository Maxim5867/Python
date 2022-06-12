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
[0] |
/|\ |
/ \ |
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

def LevelVibor():
    print('Выберите уровень сложности')
    print('Введите "L" для легкого')
    print('Введите "S" для среднего')
    print('Введите "T" для тяжелого')
    while True:
        otv = input().upper()
        if len(otv) !=1:
            print('Введите только одну букву')
        elif otv not in 'LST':
            print('Введите "L" для легкого'
    'Введите "S" для среднего'
    'Введите "T" для тяжелого')
        else:
            return otv

def deletVis(urS):
    if LevelVibor == 'S':
        del HANGMANPICS[10]
        del HANGMANPICS[9]
    elif LevelVibor == 'T':
        del HANGMANPICS[10]
        del HANGMANPICS[9]
        del HANGMANPICS[8]
        del HANGMANPICS[7]

bS = LevelVibor()
deletVis(bS)

for i in range(len(HANGMANPICS)-1):
    print(HANGMANPICS[i])
            
