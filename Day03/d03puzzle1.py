"""
Advent of code 2022
Day 3 - puzzle 1

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

with open('/home/tom/Bureau/Developpement/AdventOfCode/Input/d03input.txt', 'r') as inputFile :
    inputRucksack = inputFile.readlines()


dictOfPriorities = dict()
for elem in string.ascii_lowercase :
    dictOfPriorities[elem] = ord(elem)-96

for elem in string.ascii_uppercase :
    dictOfPriorities[elem] = ord(elem)-38

listofPriorities = []
for elem in inputRucksack :
    firstCompartment = elem[:len(elem)//2]
    secondCompartment = elem[len(elem)//2:]

    for elem in firstCompartment :
        if elem in secondCompartment :
            listofPriorities.append(dictOfPriorities[elem])
            break
        
print("Sum of priorities:", sum(listofPriorities))
