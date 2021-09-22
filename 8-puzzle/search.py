import puzzle8 as p8
import math

def numWrongTiles(state):
    count = 0
    for i in range(0,9):
        if(p8.getTile(state,i) != p8.getTile(p8._goal,i) and p8.getTile(state,i) != 0):
            count += 1
    return count


def manhattanDistance(state):
    count = 0
    for i in range(0,9):
        for j in range(0,9):
            if(p8.getTile(state,i) == p8.getTile(p8._goal,j) and p8.getTile(state,i) != 0):
                count += abs(i%3 - j%3) + abs(math.floor(i/3) - math.floor(j/3))
    return count