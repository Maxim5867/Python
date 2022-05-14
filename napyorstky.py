#Игра наперстки
import random,time

def myPred():
    print('''Игрок пошел на рынок.
    Зайдя на рынок он увидел мужчину,
    который сидит за столом.''')
    time.sleep(2)
    print('''На столе перед человеком стояли три
    наперстка. Он показал шарик и накрыл его одним наперстком...''')
    time.sleep(2)

def myIst():
    print('''Началась игра, и ведущий начал перебирать наперстки''')
    time.sleep(2)
    print('''Он остановил движение наперстков и спросил
    в каком наперстке шарик''')

def myGames():
    select = random.randint(1,3)
    print('''Введите число для выбора наперстка "1", "2", "3".''')
    vybor = input()
    while vybor !='1' and vybor != '2' and vybor !='3':
        print('Необходимо ввести "1","2" или "3".')
        vybor = input()
    print('Ведущий поднял наперсток, который вы выбрали...')
    time.sleep(2)
    if select == int(vybor):
        print('''... и под наперстком было пусто.
        'вы проиграли' - ''')

myPred()
doneGames = 'да'
while doneGames == 'да' or doneGames == 'д':
    myIst()
    myGames()
    print('''Вы хотите сыграть еще раз?".''')
    doneGames = input()
    
