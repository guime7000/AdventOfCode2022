"""
Advent of code 2022
Day 5 - puzzle 2

Thomas Guimezanes.

Solved in 10 minutes
"""
from collections import deque

# Website Example
# inputCranes=[
#             '    [D]    ',
#             '[N] [C]    ',
#             '[Z] [M] [P]',
#             ' 1   2   3 ',
#             '\n',
#             'move 1 from 2 to 1',
#             'move 3 from 1 to 3',
#             'move 2 from 2 to 1',
#             'move 1 from 1 to 2']

# website example param
# nbTowers = 3
# nbRows = 3

with open('/url/to/input/file','r') as inputFile :
    inputCranes = inputFile.readlines()

nbTowers = 9
nbRows = 8
towers = {}

for i in range(nbTowers):
    towers[i+1] = deque()

# creates towers
towerNumber = [k for k in range(1,3*nbTowers+(nbTowers -1),4)]
for elem in inputCranes[0:nbRows]:
    for i in range(nbTowers):
        if ord(elem[towerNumber[i]]) != 32:
            towers[i+1].append((elem[towerNumber[i]]))

moves = []
# create Moves list
for elem in inputCranes[nbRows+2:] :
    tmplist =[]
    for cell in elem.rsplit():
        if cell.isnumeric():
            tmplist.append(cell)    
    moves.append(tmplist)

for elem in moves :
    nbCrates = int(elem[0])
    fromTower = int(elem[1])
    toTower = int(elem[2])

    tempCratePile = []
    for i in range(nbCrates):
        tempCratePile.append(towers[fromTower].popleft())
        print(tempCratePile)
    for crate in tempCratePile[::-1] :
        towers[toTower].appendleft(crate)
    print(towers.items())
outString = []       
for k in towers.keys():
    print(towers[k][0],end='')
print("\n")









