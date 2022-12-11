"""
Advent of code 2022
Day 10 - puzzle 2

Thomas Guimezanes.

Solved in  minutes 
"""

import os

# Website Example
# inputFileName = 'd010Websiteinput.txt'


inputFileName = 'd010input.txt'
with open(os.path.join('/path/to/directory/containing/inputFile', inputFileName),'r') as inputFile :
    inputSequence = inputFile.readlines()

cycleCounter = 0
xRegister = [1]

crtWidth = 40
renderingOnScreen=[]

for line in inputSequence:
    operation = line.rsplit()
    cycleCounter += 1
    xRegister.append(xRegister[-1])

    if operation[0] == 'addx':
        xRegister.append(xRegister[-1] + int(operation[-1]))
        cycleCounter += 1
        
rowCount = 0      
for cycle in range(1,len(xRegister)):
    cycle2 = cycle%crtWidth
    leftSprite = xRegister[cycle-1]-1
    sprite = xRegister[cycle-1]
    rightSprite = xRegister[cycle-1]+1
    if ((xRegister[cycle-1]) <= cycle2 <= (xRegister[cycle-1]+2)) :
        renderingOnScreen.append('#')
    else :
        renderingOnScreen.append('.')
    if cycle%crtWidth == 0 :
        rowCount += 1

# Rendering :
with open('/path/where/you:want/to/save/your/final/render','w') as renderFile :
    for i,point in enumerate(renderingOnScreen,1):
        renderFile.write(point)
        if i%40 == 0:
            renderFile.write('\n')
