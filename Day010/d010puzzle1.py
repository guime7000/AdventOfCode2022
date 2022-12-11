"""
Advent of code 2022
Day 10 - puzzle 1

Thomas Guimezanes.

Solved in  40 minutes 
"""

from collections import defaultdict
from math import sqrt
import numpy as np
import os

def signal_strength(inCyclesNumber : list, inXRegister: list) -> list :
    """
    Calculates the signal strength for the cycles number set in inCyclesNumber 

    returns a list of the same length as inCycleNumber containing the signal strength of the inXRegister at inCycleNumber cycles.
    """
    outSignalStrength = []
    for cycle in inCyclesNumber :
        outSignalStrength.append(inXRegister[cycle-1] * cycle)

    return outSignalStrength

# Website Example
# inputFileName = 'd010Websiteinput.txt'


inputFileName = 'd010input.txt'
with open(os.path.join('/url/to/input/file/directory', inputFileName),'r') as inputFile :
    inputSequence = inputFile.readlines()

cycleCounter = 0
xRegister = [1]

for line in inputSequence:

    operation = line.rsplit()
    cycleCounter += 1
    xRegister.append(xRegister[-1])

    if operation[0] == 'addx':
        xRegister.append(xRegister[-1] + int(operation[-1]))
        cycleCounter += 1

cycleList = [20, 60, 100, 140, 180, 220]
signalStrength = signal_strength(cycleList,xRegister)

print("Signal strength :", sum(signalStrength))
