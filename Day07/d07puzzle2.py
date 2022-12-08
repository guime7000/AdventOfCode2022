"""
Advent of code 2022
Day 7 - puzzle 2

Thomas Guimezanes.

Solved in 7 minutes
"""

from collections import deque, defaultdict

# Website Example
# inputSequence =['$ cd /\n',
#                 '$ ls\n',
#                 'dir a\n',
#                 '14848514 b.txt\n',
#                 '8504156 c.dat\n',
#                 'dir d\n',
#                 '$ cd a\n',
#                 '$ ls\n',
#                 'dir e\n',
#                 '29116 f\n',
#                 '2557 g\n',
#                 '62596 h.lst\n',
#                 '$ cd e\n',
#                 '$ ls\n',
#                 '584 i\n',
#                 '$ cd ..\n',
#                 '$ cd ..\n',
#                 '$ cd d\n',
#                 '$ ls\n',
#                 '4060174 j\n',
#                 '8033020 d.log\n',
#                 '5626152 d.ext\n',
#                 '7214296 k\n']


with open('/url/to/input/file','r') as inputFile :
    inputSequence = inputFile.readlines()

directorySize = defaultdict(list)
currentStack = []
currentPath = ""

totalDiskSPace = 70_000_000
unusedNeededSpace = 30_000_000
freeSpace = totalDiskSPace - directorySize['/']
toBeFreeed = unusedNeededSpace - freeSpace

for line in inputSequence :
    splittedLine = line.rsplit()
    if splittedLine[0] == "$" :
        if splittedLine[1] == 'cd':
            
            if splittedLine[-1] != ".." and splittedLine[-1] != "/":
                currentPath += f"/{splittedLine[-1]}" if currentPath != "/" else splittedLine[-1]
                currentStack.append(currentPath)
                directorySize[currentPath] = 0
            
            elif splittedLine[-1] == "/":
                currentPath="/"
                currentStack=["/"]
                directorySize[currentPath] = 0
            
            elif splittedLine[-1] == ".." :
                currentPath = "/".join(currentPath.split("/"))[:-1]
                currentStack.pop()

    if splittedLine[0].isnumeric():
        fileSize = int(splittedLine[0])
        for directories in currentStack :
            directorySize[directories] += fileSize


deletable = [directory for directory in directorySize.values() if directory >= toBeFreeed]
print(min(deletable))