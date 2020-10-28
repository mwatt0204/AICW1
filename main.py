# This is a sample Python script.

import sys
import copy
import  time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


timesran = 0



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


def DFID(path):
    soloution = None
    depth = 1
    while (soloution == None):
        soloution = dfd(path, depth)
        depth = depth + 1  # if no soloutin found incremnt depth by 1
    return soloution


def dfd(path, maxDepth):
    global timesran
    if isGoalState(path[-1]):  # indexing from last so -1 is last iteam in path
        return path
    if maxDepth <= 0:
        return None

    else:
        laststate = copy.deepcopy(path[-1])  #deep copy as move method yeilds
        for nextState in move(laststate):
            timesran = timesran + 1  ## count nubmer of moves made
            if nextState not in path:
                nextPath = path + [nextState]  # adds iteam to array at end
                solution = dfd(nextPath, maxDepth - 1)
                if solution is not None:  # maybe this line
                    return solution
    return None



def DFIDWithTmingsandMovesandLengths(state):
    path = [state]
    global timesran
    timesran = 0
    startTime = time.time()
    soloutin = DFID(path)
    endTime = time.time()
    runtime = endTime-startTime
    return soloutin,timesran,runtime


def stateToString(state):
    [i, j, grid] = state
    for rows in grid:
        for item in rows:
            print(item, end=' ')
        print()
    print('\n')



def runFromCSV(file):

    sloution,moves,time = DFIDWithTmingsandMovesandLengths(state)
    print(len(sloution)-1,":Shortest number of Moves")
    print(moves , "moves in path")
    print(time, "seconds")






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    state = [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]]

#    path = [state]
 #   print(DFID(path))
    # print(dfs(path, 16))
  #  print(timesran)

    sloution,moves,time = DFIDWithTmingsandMovesandLengths(state)
    print(len(sloution)-1,":Shortest number of Moves")
    print(moves , "moves in path")
    print(time, "seconds")