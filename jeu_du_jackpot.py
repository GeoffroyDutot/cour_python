#1. Jeu du jackpot

import random
jackpot = random.randint(1,1001)
essai = input("Proposer un nombre : ")

for nb_essai in range(10):
    print("Essai n° ",nb_essai+1,":")

    if jackpot > int(essai):
        print("le jackpot est plus grand")
    else:
        print("le jackpot est plus petit")

    if jackpot == int(essai):
        print("Bravo vous avez gagné ! ")
        exit()
    else:
        print("Proposer un nouvel essai")
        essai = input("Numéro choisi : ")
        essai= int(essai)
print("Raté ! Vous n'avez plus d'essais.. Le jackpot était : ",jackpot)
