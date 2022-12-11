"""
Advent of code 2022
Day 9 - puzzle 1

Thomas Guimezanes.

Solved in  minutes 
"""

from collections import defaultdict
from math import sqrt
import numpy as np

def update_points_position(inDirection: str, inStep: int, inCoords : list) -> list:
    """
    updates (inX, inY) point's absolute position in the plane by inStep depending on the inDirection order received ( 'R'ight, 'L'eft, 'U'p or 'D'own)

    returns a [X,Y] list of the point's updated position
    """
    inX, inY = inCoords

    if inDirection == 'R' :
        return [inX + inStep, inY]
    
    if inDirection == 'L' :
        return [inX - inStep, inY]

    if inDirection == 'U' :
        return [inX, inY + inStep]
    
    if inDirection == 'D' :
        return [inX, inY - inStep]

def computes_head_tail_distance(inHeadCoords : list, inTailCoords : list) -> int :
    """
    computes plane distance between two points
    """

    headX, headY = inHeadCoords
    tailX, tailY = inTailCoords

    return sqrt((headX-tailX)**2 + (headY-tailY)**2)

def computes_scalar_product(inPoint1 : list, inPoint2 : list, axis: str) -> float :
    """
    builds the vector1 from inPoint1 and inPoint2 coords
    
    returns the dot product between vector1 and i vector if axis = 'i'
    returns the dot product between vector1 and j vector if axis = 'j'
    """
       
    x1,y1 = inPoint1
    x2,y2 = inPoint2

    vector1 = np.array([x2-x1, y2-y1])
    if axis == 'i' :
        vector2 = np.array([1,0])
    if axis == 'j' :
        vector2 = np.array([1,0])

    return np.dot(vector1,vector2)

# Website Example
# inputSequence =["R 4\n",
#                 "U 4\n",
#                 "L 3\n",
#                 "D 1\n",
#                 "R 4\n",
#                 "D 1\n",
#                 "L 5\n",
#                 "R 2\n"]

with open('/path/to/input/file','r') as inputFile :
    inputSequence = inputFile.readlines()

offset = 1 # head and tail are 1 postion away from each other
maxTouchingDist = sqrt(2*offset**2)

currentHeadPosition = [0,0]
currentTailPosition = [0,0]

visitedHead = [[0,0]]
visitedTail=defaultdict(list) # stores all visited positions of the tail (needed for answering the puzzle) with keys as X postition and values as Y positions

outofdist = 0
for line in inputSequence:
    move = line.rsplit()
    for i in range(int(move[-1])):
        currentHeadPosition = update_points_position(move[0], offset, currentHeadPosition)
        visitedHead.append(currentHeadPosition)
        if computes_head_tail_distance(currentHeadPosition,currentTailPosition) <= maxTouchingDist :
            if currentTailPosition[1] not in visitedTail[currentTailPosition[0]]:
                visitedTail[currentTailPosition[0]].append(currentTailPosition[1])
        else :
            outofdist += 1
            dotX = computes_scalar_product(currentHeadPosition,currentTailPosition,'i')
            dotY = computes_scalar_product(currentHeadPosition,currentTailPosition,'j')

            previousHeadPosition = visitedHead[-2]
            currentTailPosition[0] = previousHeadPosition[0]
            currentTailPosition[1] = previousHeadPosition[1]
            
            if dotX == 0 :
                if dotY > 0 :
                    currentTailPosition[1] -= 1
                if dotY < 0 :
                    currentTailPosition[1] += 1
                    
            if dotY == 0:
                if dotX > 0 :
                    currentTailPosition[0] -= 1
                if dotX < 0 :
                    currentTailPosition[0] += 1

            if (dotX != 0 and dotY !=0) :
                previousHeadPosition = visitedHead[-2]
                currentTailPosition[0] = previousHeadPosition[0]
                currentTailPosition[1] = previousHeadPosition[1]
            if currentTailPosition[1] not in visitedTail[currentTailPosition[0]]:
                visitedTail[currentTailPosition[0]].append(currentTailPosition[1])

positionsCounter = 0
for k in visitedTail.keys():
    for elem in visitedTail[k]:
        positionsCounter += 1

print("Answer : ",positionsCounter)