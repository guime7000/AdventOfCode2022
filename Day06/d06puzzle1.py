"""
Advent of code 2022
Day 6 - puzzle 2

Thomas Guimezanes.

Solved in 20 minutes 
"""
from collections import deque

def is_duplicated(inDeque):
    """
    checks if there is a duplicated letter in the inDeque

    returns True if inLetter in the deque, False otherwise
    """
    dequeLength = len(inDeque)
    for i in range((dequeLength)) :
        if inDeque[i] in list(inDeque)[i+1:]:
            return True
    
    return False


# Website Example
# inputSequence=['mjqjpqmgbljsphdztnvjfqwrcgsmlb',
#                'bvwbjplbgvbhsrlpgdmjqwftvncz', 
#                 'nppdvjthqldpwncqszvftbrmjlhg',
#                 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
#                 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']

 with open('/url/to/input/file','r') as inputFile :
    inputSequence = inputFile.readlines()

lengthOfStartOf = 4 #length of queue 

for sequence in inputSequence :
    currentStack = deque(sequence[:lengthOfStartOf])
    for j, letter in enumerate(sequence[lengthOfStartOf:]):
        if is_duplicated(currentStack):
            currentStack.popleft()
            currentStack.append(letter)
        else:
            print("Marker position:" ,j+lengthOfStartOf)
            break









