# This is a sample Python script.

import sys
import copy

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


timesran = 0


# sys.setrecursionlimit(4000)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def move_blank(i, j, n):
    if i + 1 < n:
        yield (i + 1, j)
    if i - 1 >= 0:
        yield (i - 1, j)
    if j + 1 < n:
        yield (i, j + 1)
    if j - 1 >= 0:
        yield (i, j - 1)


def move(state):
    [i, j, grid] = state
    n = len(grid)
    for pos in move_blank(i, j, n):
        i1, j1 = pos
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
        yield [i1, j1, grid]
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]


def isGoalState(state):
    [i, j, grid] = state
    x = 0
    for rows in grid:
        for item in rows:
            if item != x + 1:
                return False
            x = x + 1
            if x == 8:
                print("yes")
                return True


viewed = []


def dfs2(currentState, maxDepth):
    global viewed
    viewed = viewed + [currentState]
    global timesran
    timesran = timesran + 1

    if isGoalState(currentState): return True

    if maxDepth <= 0: return False

    for nextState in move(currentState):
        if nextState not in viewed:
            # print(nextState)
            stateToString(nextState)
            if dfs2(nextState, maxDepth - 1):
                return True
    return False


def dfsMain(path):
    soloution = None
    depth = 1
    while (soloution == None):
        soloution = dfs(path, depth)
        depth = depth + 1
        print(depth)
    return soloution


def dfs(path, maxDepth):
    global timesran
    timesran = timesran + 1
    if isGoalState(path[-1]):  # indexing from last so -1 is last iteam
        return path[-1]
    if maxDepth <= 0:
        return None

    else:
        laststate = path[-1]
        for nextState in move(laststate):
           # print(not inpath(nextState, path))
            if not inpath(nextState, path):  # think issue is with comaring
                nextPath = copy.deepcopy(path) + [nextState]  # adds iteam to array at end
                solution = dfs(nextPath, maxDepth - 1)
                if solution != None:  # maybe this line
                    return dfs(nextPath, maxDepth + 1)
    return None


def inpath(state, path):
    #   inpath = False
    [i, j, grid] = state
    for iteams in path:
        [i2, j2, grid2] = iteams
        if i == i2:
            if j == j2:
                for x in range(3):
                    for r in range(3):
                        if grid2[x][r] == grid[x][r]:
                            return True
    return False

# path needs to be node at start
def idfs(node, currentDepth, maxDepth, path):
    if isGoalState(node.state):
        return node, True

    for nextState in move(node.state):
        if nextState not in path:
            child = Node(nextState, [], node)
            node.children = node.children + [child]
            path = path + [nextState]

    if currentDepth == maxDepth:
        if len(node.children) > 0:
            return None, False
        else:
            return None, True

    reachedEnd = True
    for i in range(len(node.children)):
        nextPath = copy.deepcopy(path) + [node.children[i]]
        soloution, reachedEnd2 = idfs(node.children[i], currentDepth + 1, maxDepth, nextPath)

        if soloution != None:
            return soloution, True

        reachedEnd = reachedEnd2 and reachedEnd

    return None, reachedEnd


class Node:
    def __init__(self, state, children, parent):
        self.state = state
        self.children = children
        self.parent = parent


def stateToString(state):
    [i, j, grid] = state
    for rows in grid:
        for item in rows:
            print(item, end=' ')
        print()
    print('\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # state = [2,1, [[1, 2, 3], [4,5,6], [7, 0, 8]]]
    # state = [1, 1, [[3, 7, 1], [4, 0, 2], [8, 6, 5]]]
    state = [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]]

    # goalState = [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
    # stateToString(goalState)
    # print(isGoalState(goalState))
    # print(isGoalState([2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]))

    # stateToString(state)
    # for nextState in move(state):
    # print(nextState)
    # stateToString(nextState)
    path = [state]
    dfsMain(path)
    #print(dfs(path, 100))
    print(timesran)

# print(dfsMain(path))

# depth = 1
# br = False
# node = Node(state, [], None)
# while not br:
#     soloution, br = idfs(node, 0, depth, path)
#    if (soloution is not None):
#       print(soloution)
#      break
#  depth *= 2
#  print("depth incressed")

#  print("END")
#  print(timesran)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
