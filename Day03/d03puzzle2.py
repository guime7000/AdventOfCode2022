"""
Advent of code 2022
Day 3 - puzzle 2

Thomas Guimezanes.

"""

import string

#### Test example of website #####
# inputRucksack = ['vJrwpWtwJgWrhcsFMMfFFhFp',
#                 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
#                 'PmmdzqPrVvPwwTWBwg',
#                 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
#                 'ttgJtRGJQctTZtZT',
#                 'CrZsJsPPZsGzwwsLwLmpwMDw',
#                 ]

with open('/url/to/input/file', 'r') as inputFile :
    inputRucksack = inputFile.readlines()

dictOfPriorities = dict()
for elem in string.ascii_lowercase :
    dictOfPriorities[elem] = ord(elem)-96
for elem in string.ascii_uppercase :
    dictOfPriorities[elem] = ord(elem)-38

listOfElvesPackage = []
for i in range(0,len(inputRucksack)-1,3):
    listOfElvesPackage.append(inputRucksack[i:i+3])

listOfPriorities = []
for listGroup in listOfElvesPackage :
    listGroup.sort(key = len , reverse = True)
    for packItem in listGroup[0]:
        if ((packItem in listGroup[1]) and (packItem in listGroup[2])):
            listOfPriorities.append(dictOfPriorities[packItem])
            break

print("Sum of priorities:", sum(listOfPriorities))
