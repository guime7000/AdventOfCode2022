"""
Advent of code 2022
Day 2 - puzzle 1

Thomas Guimezanes.


First column (opponent's choice)
A : Rock
B : Paper
C : Scissors

Second column (my choice)
X: Rock (1 pt)
Y: Paper (2 pt)
Z: Scissors (3 pt)

Loss : 0 pt | Draw : 3 pt | Win : 6 pt

AX : 1 + 3 = 4 | BX : 1 + 0 = 1 | CX : 1 + 6 = 7
AY : 2 + 6 = 8 | BY : 2 + 3 = 5 | CY : 2 + 0 = 2
AZ : 3 + 0 = 3 | BZ : 3 + 6 = 9 | CZ : 3 + 3 = 6

"""

with open('/url/to/input/file','r') as inputFile :
    inputRound = inputFile.readlines()

finalScore= 0    
scoreDict = {'A X' : 4,
            'A Y' : 8,
            'A Z' : 3,
            'B X' : 1,
            'B Y' : 5,
            'B Z' : 9,
            'C X' : 7,
            'C Y' : 2,
            'C Z' : 6}

for elem in inputRound:
    roundDictKey = " ".join(elem.rsplit())
    finalScore += scoreDict[roundDictKey]

print(finalScore)