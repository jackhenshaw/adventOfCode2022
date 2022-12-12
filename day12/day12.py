from string import ascii_lowercase
from heapq import heappop, heappush # use heaps to maintain priority queues

def neighbours(grid, index):
    # grid is elevation map
    for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]: # up, down, left, right
        i = index[0] + di
        j = index[1] + dj

        # check still on grid
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            continue

        # check heights of surrounding
        #if (grid[i][j] <= grid[index[0]][index[1]] + 1): # originally forwards search (p1)
        if (grid[i][j] >= grid[index[0]][index[1]] - 1): # changed to backward search for p2
            yield i, j

data = open("input.txt").read().strip()
lines = [line for line in data.split("\n")]

# create starting map and make elevation matrix
start_map = [list(line) for line in lines]
elevation = []
for line in lines:
    line = line.replace('S','a').replace('E','z')
    elevation.append([ascii_lowercase.index(letter) for letter in list(line)])

# find start and end goals
for i in range(len(start_map)):
    for j in range(len(start_map[0])):
        if start_map[i][j] == 'S':
            starting_index = [i, j]
        if start_map[i][j] == 'E':
            ending_index = [i, j]

# store list of visited nodes -> no point going back to them
visited = [ [ False for column in range(len(start_map[0]))] for row in range(len(start_map))]

## implement djikstra's algorithm
# originally was searching forwards for p1, but modified to search backwards to
# accomodate p2 in the same search

solvedp2 = False
heap = [(0, ending_index)] # (number of steps currently taken, current index)
while True:
    nSteps, current_index = heappop(heap)

    if visited[current_index[0]][current_index[1]]: continue # skip if already visited
    visited[current_index[0]][current_index[1]] = True

    if (not solvedp2 and elevation[current_index[0]][current_index[1]] == 0):
        solvedp2 = True
        print(f"p2: Shortest number of steps to go from E to 0 was {nSteps}")

    # if hit end position -> exit early printing the number of steps
    if ( current_index[0]==starting_index[0] and current_index[1]==starting_index[1] ):
        print(f"p1: Shortest number of steps to go from E to S was {nSteps}")
        break

    # generate next nodes to go visit from this one
    for new_index in neighbours(elevation, current_index):
        heappush(heap, (nSteps+1, new_index))
