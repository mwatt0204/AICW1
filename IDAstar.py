# g(n) length of the path
# h(n) num misplaced tiles number of tiles not in right place of tile
# g(n) + h(n) = f


import copy
import time

timesran = 0
goalState = [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]


#pires method not changed
def move_blank(i, j, n):
    if i + 1 < n:
        yield (i + 1, j)
    if i - 1 >= 0:
        yield (i - 1, j)
    if j + 1 < n:
        yield (i, j + 1)
    if j - 1 >= 0:
        yield (i, j - 1)


#pires method not chagned
def move(state):
    [i, j, grid] = state
    n = len(grid)
    for pos in move_blank(i, j, n):
        i1, j1 = pos
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
        yield [i1, j1, grid]
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]



#not used carried over form part 1
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




# returns how many valeus are not in the right place

#dosnt work like this becuse obliceus one space awoay not difrence of 1

def missmatchedGoalState(state):
    [i, j, grid] = state
    missmatched = 0
    x = 0
    for row in range(len(grid)):
        for item in range(len(grid[row])):
            if x == 8:
                if grid[row][item] != 0:
                    z,y = getpostioningoalState(grid[row][item])
                    missmatched = missmatched + (abs(z-row) + abs(y - item))
                #print(missmatched)
                return missmatched
            if grid[row][item] != x + 1:
                z, y = getpostioningoalState(grid[row][item])
                missmatched = missmatched + (abs(z - row) + abs(y - item))
            x = x + 1


def getpostioningoalState(value):
    [x,y, goalgrid] = goalState
    for r in range(len(goalgrid)):
        try:
            postion = goalgrid[r].index(value)
            return r,postion
        except Exception:
            pass
    print("fallthorugh")



def IDAstart(state):
    sloution = None
    bound = 1 + missmatchedGoalState(state)
    path = [state]
    while sloution is None:  #runs untill soulouting is found
        sloution, newbound = IDAstar(path, bound)
        bound = newbound
    return sloution


def IDAstar(path, bound):
    global timesran
    g = len(path)
    h = missmatchedGoalState(path[-1])
    f = g + h       ## bound value of sate path[-1]
    if f > bound:
        return None, f
    if h == 0:          ## if none are missmatched then is goal state
        return path, f

    laststate = copy.deepcopy(path[-1])  # deep copy as move method yeilds
    min = float('inf')  # set min to infinty
    for nextState in move(laststate):
        timesran = timesran + 1
        if nextState not in path:
            nextpath = path + [nextState]
            soloution, newbound = IDAstar(nextpath, bound)
            if soloution != None: # golestate found
                return soloution, newbound
            if newbound < min:
                min = newbound
    return None, min




# method to genororate timing and rest timesRan vaeriable between each call
def IDAWithTmingsandMovesandLengths(state):
    global timesran
    timesran = 0
    startTime = time.time()
    soloutin = IDAstart(state)
    endTime = time.time()
    runtime = endTime - startTime
    return soloutin, timesran, runtime


if __name__ == '__main__':

    # array of states given in brefi
    startStates = [
        [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]],
        [0, 2, [[5, 6, 0], [1, 3, 8], [4, 7, 2]]],
        [2, 0, [[3, 5, 6], [1, 2, 7], [0, 8, 4]]],
        [1, 1, [[7, 3, 5], [4, 0, 2], [8, 1, 6]]],
        [2, 0, [[6, 4, 8], [7, 1, 3], [0, 2, 5]]],
        [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]],
        [0, 0, [[0, 1, 8], [3, 6, 7], [5, 4, 2]]],
        [2, 0, [[6, 4, 1], [7, 3, 2], [0, 5, 8]]],
        [0, 0, [[0, 7, 1], [5, 4, 8], [6, 2, 3]]],
        [0, 2, [[5, 4, 0], [2, 3, 1], [8, 7, 6]]],
        [2, 1, [[8, 6, 7], [2, 5, 4], [3, 0, 1]]]
    ]

    for state in startStates:
        sloution, moves, timetaken = IDAWithTmingsandMovesandLengths(state)
        print(len(sloution) - 1, ":Shortest number of Moves")
        print(moves, "moves in path")
        print(timetaken, "seconds")

