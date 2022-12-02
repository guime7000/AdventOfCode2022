"""
Advent of code 2022
Day 1 - puzzle 2

Thomas Guimezanes.
"""


with open('/url/to/input/file','r') as inputFile :
    inputCalories = inputFile.readlines()

listCalories = []
sommeCalories = 0
for elem in inputCalories :
    calorie = elem.rsplit()
    print(calorie, sommeCalories)
    if len(calorie):
        sommeCalories += int(calorie[0])
        # if sommeCalories > maxCalories :
        #     maxCalories = sommeCalories
    else :
        listCalories.append(sommeCalories)
        sommeCalories = 0

listCalories.sort()
print(listCalories)

print("Max Calories of first three:", listCalories[-1] + listCalories[-2] + listCalories[-3])
        
    


# print(inputCalories[0:10])