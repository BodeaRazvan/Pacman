import random

maxX = 30
maxY = 30

# write mode just to clear the file at the start
file1 = open("newGrid.lay", 'w')
open("newGrid.lay", 'a')

mapMatrix = [[0] * maxX for i in range(maxY)]
choiceList = [1, 2, 3, 4]

# generating random locations for the walls
# this generation will be the starting grownd for modifications
for x in range(maxX):
    for y in range(maxY):
        if x == 0 or y == 0 or x == maxX - 1 or y == maxY - 1:
            mapMatrix[x][y] = 1
        else:
            k = random.choice(choiceList)
            if k == 1:
                mapMatrix[x][y] = 1
            else:
                mapMatrix[x][y] = 0

# making sure the map can be played and every place is reachable 
# by removing walls that would block the path
for x in range(maxX - 1):
    for y in range(maxY - 1):
        # a space surrounded by 3 walls
        if (mapMatrix[x - 1][y] == 1 and mapMatrix[x + 1][y] == 1 and mapMatrix[x][y - 1] == 1) or (
                mapMatrix[x + 1][y] == 1 and mapMatrix[x][y - 1] == 1 and mapMatrix[x][y + 1] == 1) or (
                mapMatrix[x - 1][y] == 1 and mapMatrix[x + 1][y] == 1 and mapMatrix[x][y + 1] == 1):
            if x != 0 and x + 1 != maxX - 1 and y != 0 and y + 1 != maxY - 1:
                choice = random.choice(choiceList)
                if choice == 1:
                    if x-1 != 0:
                        mapMatrix[x - 1][y] = 0
                if choice == 2:
                    if x + 1 != maxX-1:
                        mapMatrix[x + 1][y] = 0
                if choice == 3:
                    if y-1 != 0:
                        mapMatrix[x][y - 1] = 0
                if choice == 4:
                    if y+1 != maxY-1:
                        mapMatrix[x][y + 1] = 0

for x in range(maxY - 1, 1, -1):
    if mapMatrix[1][x] == 0:
        mapMatrix[1][x] = 2
        break
for y in range(1, maxY - 1, 1):
    if mapMatrix[maxX-2][y] == 0:
        mapMatrix[maxX-2][y] = 3
        break

# writing the matrix in a file as a format that can be understood by the pacman program
ok = 0
for x in range(maxX):
    for y in range(maxY):
        if mapMatrix[x][y] == 1:
            file1.write('%')
        if mapMatrix[x][y] == 0:
            file1.write(' ')
        if mapMatrix[x][y] == 2:
            file1.write('P')
        if mapMatrix[x][y] == 3:
            file1.write('.')
    file1.write('\n')
