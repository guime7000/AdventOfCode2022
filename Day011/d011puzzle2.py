"""
Advent of code 2022
Day 11 - puzzle 1

Thomas Guimezanes.

Solved in 30 minutes 
"""

from collections import defaultdict
from math import sqrt, floor
import numpy as np
import os

# Website Example
# monkeyDict = {0 : {'items' : [79,98], 'operation' : 'worryLevel*19/3', 'test' : 23, 'true' : 2, 'false' : 3, 'counter' : 0},
#               1 : {'items' : [54, 65, 75, 74], 'operation' : '(worryLevel+6)/3', 'test' : 19, 'true' : 2, 'false' : 0, 'counter' : 0},
#               2 : {'items' : [79, 60, 97], 'operation' : '(worryLevel**2)/3', 'test' : 13, 'true' : 1, 'false' : 3, 'counter' : 0},
#               3 : {'items' : [74],'operation' : '(worryLevel+3)/3', 'test' : 17, 'true' : 0, 'false' : 1, 'counter' : 0}
#               }              


# inputFileName = 'd010Websiteinput.txt'
def append_item_to_next_monkey(inMonkeyList : list, inMonkeyDict: dict) -> dict:
    """
    For each turn, "moves" one item to another monkeys list of item

    inMonkeyList : list of monkeys numbers for this turn

    returns updated np.array of item for a given monkey in inMonkeyDict.
    """
    outMonkeyDict = inMonkeyDict.copy()

    for monkey in inMonkeyList:
        itemsList = outMonkeyDict[monkey]['items']
        trueMonkey = outMonkeyDict[monkey]['true']
        falseMonkey = outMonkeyDict[monkey]['false']
        for worryLevel in itemsList :
            # newWorryLevel = floor(eval(outMonkeyDict[monkey]['operation'],{'worryLevel' : worryLevel})/3)
            newWorryLevel = eval(outMonkeyDict[monkey]['operation'],{'worryLevel' : worryLevel})
            if newWorryLevel%outMonkeyDict[monkey]['test'] == 0:
                outMonkeyDict[trueMonkey]['items'].append(newWorryLevel)
            else :
                outMonkeyDict[falseMonkey]['items'].append(newWorryLevel)
        # for elem in itemsList:
        outMonkeyDict[monkey]['counter'] = outMonkeyDict[monkey]['counter'] + len(itemsList)
        outMonkeyDict[monkey]['items'] = []

    return outMonkeyDict

# inputFileName = 'd010input.txt'
# with open(os.path.join('/url/to/input/file/directory', inputFileName),'r') as inputFile :
#     inputSequence = inputFile.readlines()

{'items' : [79,98], 'operation' : 'worryLevel*19/3', 'test' : 23, 'true' : 2, 'false' : 3, 'counter' : 0},

monkeyDict = {0 : {'items' : [50, 70, 89, 75, 66, 66], 'operation' : 'worryLevel*5', 'test' : 2, 'true' : 2, 'false' : 1, 'counter' : 0},
              1 : {'items' : [85], 'operation' : 'worryLevel**2', 'test' : 7, 'true' : 3, 'false' : 6, 'counter' : 0},
              2 : {'items' : [66, 51, 71, 76, 58, 55, 58, 60],'operation' : 'worryLevel+1', 'test' : 13, 'true' : 1, 'false' : 3, 'counter' : 0},
              3 : {'items' : [79, 52, 55, 51],'operation' : 'worryLevel+6', 'test' : 3, 'true' : 6, 'false' : 4, 'counter' : 0},
              4 : {'items' : [69, 92], 'operation' : 'worryLevel*17', 'test' : 19, 'true' : 7, 'false' : 5, 'counter' : 0},
              5 : {'items' : [71, 76, 73, 98, 67, 79, 99],'operation' : 'worryLevel+8', 'test' : 5, 'true' : 0, 'false' : 2, 'counter' : 0},
              6 : {'items' : [82, 76, 69, 69, 57],'operation' : 'worryLevel+7', 'test' : 11, 'true' : 7, 'false' : 4, 'counter' : 0},
              7 : {'items' : [65, 79, 86],'operation' : 'worryLevel+5', 'test' : 17, 'true' : 5, 'false' : 0, 'counter' : 0}
              }

numberOfRounds = 10_000
for i in range(numberOfRounds):
    monkeyDict = append_item_to_next_monkey([0,1,2,3,4,5,6,7],monkeyDict)

touchedItems = []
for k in monkeyDict.keys():
    touchedItems.append(monkeyDict[k]['counter'])

sortedTouchedItems = sorted(touchedItems)
# print(sortedTouchedItems)

print("Answer :", sortedTouchedItems[-1] * sortedTouchedItems[-2] )