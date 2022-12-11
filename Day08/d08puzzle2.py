"""
Advent of code 2022
Day 8 - puzzle 2

Thomas Guimezanes.

Solved in 45 minutes
"""

import numpy as np

def forestMapToArray(inMap: list) -> np.array:
    """
    generates, from the RAW input map, the ndarray corresponding to the forest map
    """
    mapList = []
    for treeLine in inMap :
        mapList.append([int(tree) for tree in treeLine.rsplit()[0]])
    
    return np.array(mapList, dtype='int')

def row_dist(inRowIndex: int, inColumnIndex:int, inTreeLine : np.array) -> int :
    """
    Calculates view distance on the left and right (or up and down) of a given (inRowIndex, inColumnIndex) coordinates tree on the map

    Returns the product of left and right (or up and down) distances
    """
    refHeight = inTreeLine[inColumnIndex]
    
    leftPart = np.copy(inTreeLine[0:inColumnIndex])
    rightPart = np.copy(inTreeLine[inColumnIndex+1:])

    leftBool = (leftPart < refHeight)
    rightBool = (rightPart < refHeight)

    ldist = 0
    rdist = 0

    for elem in np.flip(leftBool):
        if elem == True :
            ldist += 1
        else :
            ldist += 1
            break
    
    for elem in rightBool:
        if elem == True :
            rdist += 1
        else :
            rdist += 1
            break

    return ldist*rdist      


# Website Example
# inputSequence =["30373\n",
#                 "25512\n",
#                 "65332\n",
#                 "33549\n",
#                 "35390\n"
#                 ]


with open('/url/to/input/file','r') as inputFile :
    inputSequence = inputFile.readlines()

mapArray = forestMapToArray(inputSequence)

treeDist = []
rowDistList = []
colDistList = []

for row in range(1,mapArray.shape[0]-1):
    for col in range(1,mapArray.shape[1]-1):
        
        rowDist = row_dist(row,col,mapArray[row,:])
        colDist = row_dist(col,row,mapArray[:,col])

        treeDist.append(rowDist * colDist)

print("Maximum distance view:",max(treeDist))


