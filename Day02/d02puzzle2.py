"""
Advent of code 2022
Day 2 - puzzle 2

Thomas Guimezanes.


First column (opponent's choice)
A : Rock (1 pt)
B : Paper (2 pt)
C : Scissors (3 pt)

Second column (end of the round
X: Lose
Y: Draw
Z: Win

Loss : 0 pt | Draw : 3 pt | Win : 6 pt

AX : 3 + 0 = 3 | BX : 1 + 0 = 1 | CX : 2 + 0 = 2
AY : 1 + 3 = 4 | BY : 2 + 3 = 5 | CY : 3 + 3 = 6
AZ : 2 + 6 = 8 | BZ : 3 + 6 = 9 | CZ : 1 + 6 = 7

"""

with open('/url/to/input/file','r') as inputFile :
    inputRound = inputFile.readlines()

finalScore= 0

scoreDict = {'A X' : 3,
            'A Y' : 4,
            'A Z' : 8,
            'B X' : 1,
            'B Y' : 5,
            'B Z' : 9,
            'C X' : 2,
            'C Y' : 6,
            'C Z' : 7}

for elem in inputRound:
    roundDictKey = " ".join(elem.rsplit())
    finalScore += scoreDict[roundDictKey]

print(finalScore)