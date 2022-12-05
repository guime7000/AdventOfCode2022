"""
Advent of code 2022
Day 5 - puzzle 1

Thomas Guimezanes.

Solved in 60 minutes (45 minutes for automating inputc file reading / 15 minutes to get the answer)
"""
from collections import deque

# Website Example
# inputCranes=['    [D]    ',
#             '[N] [C]    ',
#             '[Z] [M] [P]',
#             ' 1   2   3 ',
#             '\n',
#             'move 1 from 2 to 1',
#             'move 3 from 1 to 3',
#             'move 2 from 2 to 1',
#             'move 1 from 1 to 2']
with open('/home/tom/Bureau/Developpement/AdventOfCode/Input/d05input.txt','r') as inputFile :
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


# create Moves list
moves = []
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

    for i in range(nbCrates):
        towers[toTower].appendleft(towers[fromTower].popleft())
        
for k in towers.keys():
    print(towers[k][0],end='')
print("\n")









