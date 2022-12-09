import numpy as np

f = open("input.txt", "r")

grid = []
for line in f.readlines():
    grid.append([int(num) for num in line.strip("\n")])
grid = np.array(grid)

ncol = len(grid)
nrow = len(grid[0])

visible = 2*(ncol + nrow) - 4 # subtract double counted corners
p2 = []

for r in range(1,nrow-1):
    for c in range(1,ncol-1):
        # make lists of directions to edge from this tree
        left  = grid[r][0:c][::-1]                  # reverse direction
        right = grid[r][c+1:]
        up    = [row[c] for row in grid][0:r][::-1] # reverse direction
        down  = [row[c] for row in grid][r+1:]
        directions = [left, right, up, down]

        if any([all(grid[r,c] > t for t in d) for d in directions]):
            visible += 1

        can_see = []
        for d in directions:
            for i in range(len(d)):
                if d[i] >= grid[r,c]:
                    break
            can_see.append(i+1)
        p2.append(np.prod(can_see))

print(visible)
print(max(p2))
