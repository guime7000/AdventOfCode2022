"""
Advent of code 2022
Day 1 - puzzle 1

Thomas Guimezanes.
"""


with open('/url/to/input/file','r') as inputFile :
    inputCalories = inputFile.readlines()

maxCalories = 0
sommeCalories = 0
for elem in inputCalories :
    calorie = elem.rsplit()
    print(calorie, sommeCalories)
    if len(calorie):
        sommeCalories += int(calorie[0])
        if sommeCalories > maxCalories :
            maxCalories = sommeCalories
    else :
        sommeCalories = 0
    
print("Max Calories:",maxCalories)
        