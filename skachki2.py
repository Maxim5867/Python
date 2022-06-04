import random
import time
horses = []



def play(self):
    name = input("Введите ваше имя ")
    money = 100

def placebet(self, horse, bet):
    return int(horse.odds * bet)

def winner(self):
    if self. money <= 0:
        print ('У вас не осталось денег')



def _init__(self, name, color):
    self.name = name
    self.color = color
    self.chance = random.uniform(0.5,1)
    self.odds = 1 - self.chance
    self.speed = round(self.odds*4)
    self.bet = 0
    self.position = 0
    horses.append(self)





def get_horse_pos(self):
    return self.position

def get_horse_color(self):
    return self.color[0]

def __str__(self):

    return self.name



def __init__(self, track_length):
    self.horse_num = len(horses)
    self.length = track_length

def CheckWinnerPlayer(self):
    for horse in horses:
        if horse.position >= self.length:
            print(format(horse.name))
        return horse

def print_track(self):
    for horse in horses:
        print(str(horse.name) +": ")
    for space in range(self.length):
        if space == horse.get_horse_pos():
            print(horse.name|[0], end="")
        else:
            print("_", end="")
            print()
def round(self):
    round_over = False
    winner = None
    while not round_over:
        time.sleep(1)
    self.print_track()
    winner = self.check_winner()
    if winner:
        return winner
    for horse in horses:
        horse.position += random.choice(range(horse.speed, 5))
def main(Horse,money):
    horse1 = Horse("Александр", "Красный")
    horse2 = Horse("Петр", "Синий")
    horse3 = Horse("Алексей", "Зеленый")
    horse4 = Horse("Антон", "Серый")
    for i in range(0, 4):
        if money > 0:
            print ('Ha Kakyto NOWagb Bb! XOTeNN 6bI nocTaBuTb')             
    winner = round()
    print(winner)
    if str(winner.name) == Horse:
        winnings = int((1+winner.odds))
        money += winnings
    else:
        print('BbI npourpanu! Y Bac ecTb { }" format(player.money')
    
