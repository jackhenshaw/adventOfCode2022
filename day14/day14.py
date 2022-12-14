data = open("input.txt").read().strip()

# can do this kind of on the fly rather than needing a grid
# create set of points that are rock/sand
solid = set()

for line in data.split("\n"):
    xy = [eval(l) for l in line.split("->")]
    previous = None
    for x, y in xy:
        if previous is not None:
            # find if horizontal or vertical line
            dx = int(x - previous[0])
            dy = int(y - previous[1])
            # how many solid blocks are between the two endpoints of this line
            nPoints = max(abs(dx), abs(dy)) + 1
            for i in range(nPoints):
                new_x = int(previous[0] + i*(dx/abs(dx) if dx != 0 else 0))
                new_y = int(previous[1] + i*(dy/abs(dy) if dy != 0 else 0))
                solid.add((new_x,new_y))
        previous = (x,y)

# visualise grid (maybe wrong)
#for y in range(max(y for x,y in solid)):
#    for x in range(450, 550):
#        print("#" if (x,y) in solid else ".", end='')
#    print()

abyss_start = max(y for x,y in solid)
# require floor for p2,
# decided to stretch this +- 250 as at most this would be a triangle
floor = abyss_start + 2
for x in range(250, 750):
    solid.add((x, floor))

print(f"abyss starts at {abyss_start} -> floor starts at {floor}")

p1_solved = False
for nSands in range(1000000):
    sand = (500, 0)
    while True:
        if not p1_solved and sand[1] >= abyss_start:
            print(f"p1: {nSands}")
            p1_solved = True

        if (sand[0], sand[1] + 1) not in solid: # down
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in solid: # down-left
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in solid: # down-right
            sand = (sand[0]+1, sand[1]+1)
        else: # can't move -> exit and add to set as a solid piece
            break
    solid.add(sand)

    # part 2: checking when source completely blocked
    if sand == (500, 0):
        print(f"p2: {nSands+1}")
        break
