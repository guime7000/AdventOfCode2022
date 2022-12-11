"""
Advent of code 2022
Day 8 - puzzle 1

Thomas Guimezanes.

Solved in 40 minutes
"""

import numpy as np
from collections import defaultdict

def forestMapToArray(inMap: list) -> np.array:
    """
    generates, from the RAW input map, the ndarray corresponding to the forest map
    """
    mapList = []
    for treeLine in inMap :
        mapList.append([int(tree) for tree in treeLine.rsplit()[0]])
    
    return np.array(mapList, dtype='int')

def numberOfTreesOnEdges(inArray: np.array)-> int :
    """
    returns the number of trees on the edge of the map given as an numpy array input
    """
    return 2*(inArray.shape[0]-2 + inArray.shape[1])

def row_scan(inRowIndex: int, inColumnIndex:int, inTreeLine : np.array) -> bool :
    """
    scans left part (from Row index 0 to inRowIndex) and rigth part (from inRowIndex +1 to end of the row) of the 
    inRowIndex Row for a given (inRowIndex, inColumnIndex) tree in the map

    returns:
     -True if current tree is visible
     -False otherwise.
    """

    refHeight = inTreeLine[inColumnIndex]
    
    leftPart = inTreeLine[0:inColumnIndex]
    rightPart = inTreeLine[inColumnIndex+1:]

    leftCond = np.where(leftPart >= refHeight)
    rightCond = np.where(rightPart >= refHeight)
    if (leftCond[0].size == 0 or rightCond[0].size == 0) :
        return True
    else :
        return False

# Website Example
# inputSequence =["30373\n",
#                 "25512\n",
#                 "65332\n",
#                 "33549\n",
#                 "35390\n"
#                 ]

with open('/url/to/input/file','r') as inputFile :
    inputSequence = inputFile.readlines()

visibleTreesDict = defaultdict(list)

mapArray = forestMapToArray(inputSequence)
edgesTrees = numberOfTreesOnEdges(mapArray)
visibleTreesCount = 0

for row in range(1,mapArray.shape[0]-1):
    for col in range(1,mapArray.shape[1]-1):

        if row_scan(row,col,mapArray[row,:]):
            if col not in visibleTreesDict[row]:
                visibleTreesCount += 1
                visibleTreesDict[row].append(col)

        if row_scan(col,row,mapArray[:,col]) :
            if col not in visibleTreesDict[row]:
                visibleTreesCount += 1
                visibleTreesDict[row].append(col)

print("Number of visible trees:",visibleTreesCount +  edgesTrees)
