"""
Advent of code 2022
Day 4 - puzzle 2

Thomas Guimezanes.

Solved in 20 minutes
"""
 
# Website Example
# inputPairs=['2-4,6-8',
#             '2-3,4-5',
#             '5-7,7-9',
#             '2-8,3-7',
#             '6-6,4-6',
#             '2-6,4-8']

with open('/url/to/input/file', 'r') as inputFile :
    inputPairs = inputFile.readlines()

numberOfOverlapped = 0

for pair in inputPairs :
    elveOne, elveTwo = pair.split(",")
    elveOne = list(map(int,elveOne.split("-")))
    elveTwo = list(map(int,elveTwo.split("-")))

    if (elveOne[1] >= elveTwo[0]) and (elveOne[0] <= elveTwo[1]):
        numberOfOverlapped += 1

print(numberOfOverlapped)







