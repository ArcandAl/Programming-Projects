from BlackjackNoP import *
from BlackjackStratNoP import *


games = 0
PlayerWinsBasic = 0
DealerWinsBaisc = 0
TiesBasic = 0
PlayerWinsSrat = 0
DealerWinsStrat = 0
TiesStrat = 0

for i in range(1000):
    games += 1
    resultBasic = Main()
    if resultBasic == 0:
        DealerWinsBaisc += 1
    elif resultBasic == 1:
        PlayerWinsBasic += 1
    elif resultBasic == 2:
        TiesBasic += 1

    resultStrat = main()
    if resultStrat == 0:
        DealerWinsStrat += 1
    elif resultStrat == 1:
        PlayerWinsSrat += 1
    elif resultStrat == 2:
        TiesStrat += 1


print("Games Played: ", games)
print("\nBasic Strategy")
print("Player Wins: ", PlayerWinsBasic)
print("Dealer Wins: ", DealerWinsBaisc)
print("Ties: ", TiesBasic)
print("\nPercent Player wins: {}%".format(PlayerWinsBasic / games * 100))
print("Percent Dealer wins: {}%".format(DealerWinsBaisc / games * 100))
print("Percent Ties: {}%".format(TiesBasic / games * 100))

print()

print("Developed Strategy")
print("Player Wins: ", PlayerWinsSrat)
print("Dealer Wins: ", DealerWinsStrat)
print("Ties: ", TiesStrat)

print("\nPercent Player wins: {}%".format(PlayerWinsSrat / games * 100))
print("Percent Dealer wins: {}%".format(DealerWinsStrat / games * 100))
print("Percent Ties: {}%".format(TiesStrat / games * 100))
