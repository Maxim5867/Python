from random import random
from time import time
import random
HORSESKACHKI = ['''
        
       /()
   \____|
    | |''',

]
def PredIst():
    print('''Ты пришел на 
    соревнования по скачкам''')
    print('''Ты подошел к кассе, где сидит человек''')
    print('''Перед тобой стоит выбор
     на какую лошадь поставить''')
def MyIst():
    print('''У меня есть 500 рублей''')
    print('''Есть 4 лошади''')
def MyGame():
    while True:      
        stavka = input('''Введите цифру лошади, на которую
        хотите поставить
        "1"
        "2"
        "3"
        "4" ''')
        if (stavka == 1 or stavka == 2 or stavka == 3 or stavka == 4):
             return False
        if (stavka != 1 or stavka != 2 or stavka !=3 or stavka !=4):
            return True
            print('''Введите цифру, а не другой символ''')
            
        


   