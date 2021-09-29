import puzzle8 as p8
import math
from heapq import heappush, heappop

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

def itdeep(state):
    path = None
    count = 0
    while path is None:
        path = DFS(state, count)
        count += 1
    return path
    
def DFS(state, maxDepth):
    stack = [(state, 0)]
    path = []
    for i in range(maxDepth):
        path.append(0)
    currentDepth = 0
    while len(stack) > 0:
        currentNode = stack.pop()
        currentDepth = currentNode[1]
        if currentDepth > 0:
            path[currentDepth-1] = currentNode[0]
        if currentDepth < maxDepth:
            children = findChildren(currentNode[0])
            currentDepth += 1
            for child in children:
                if child == p8.solution():
                    path[currentDepth-1] = child
                    return path
                else:
                    stack.append((child, currentDepth))
    return None

def findChildren(state):
    for i in range(9):
        if p8.getTile(state, i) == 0:
            square = i
            break
    neighbors = p8.neighbors(square)
    children = []
    for neighbor in neighbors:
        children.append(p8.moveBlank(state, neighbor))
    return children

def astar(state, heuristic):
    priority_queue = []
    head = (0, Node(state,[]))
    heappush(priority_queue,head)
    while len(priority_queue) > 0:
        currentNode = heappop(priority_queue)[1]
        if currentNode.state == p8.solution():
            return currentNode.path
        children = currentNode.find_children_nodes()
        for child in children:
            heappush(priority_queue,(len(child.path)+heuristic(child.state),child))
    return None

class Node():
    def __init__(self, state, path):
        self.state = state
        self.path = path
    
    def find_children_nodes(self):
        child_node_list = []
        for child in findChildren(self.state):
            child_path = self.path.copy()
            child_path.append(p8.blankSquare(child))
            child_node_list.append(Node(child,child_path))
        return child_node_list
    
    def __lt__(self, other):
        return True