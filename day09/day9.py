def move_knot(knot1, knot2):
    xdiff = knot1[0] - knot2[0]
    ydiff = knot1[1] - knot2[1]

    if abs(xdiff)<=1 and abs(ydiff)<=1:
        # no need to move
        pass
    elif abs(xdiff)>=2 and abs(ydiff)>=2:
        # move diagonally
        knot2 = (knot1[0]-1 if knot2[0]<knot1[0] else knot1[0]+1,
                knot1[1]-1 if knot2[1]<knot1[1] else knot1[1]+1)
    elif abs(xdiff)>=2:
        # move x-dir
        knot2 = (knot1[0]-1 if knot2[0]<knot1[0] else knot1[0]+1, knot1[1])
    elif abs(ydiff)>=2:
        # move y-dir
        knot2 = (knot1[0], knot1[1]-1 if knot2[1]<knot1[1] else knot1[1]+1)
    return knot2

f = open("input.txt", "r")

rope = [(0, 0) for _ in range(10)]

p1 = set([rope[1]])
p2 = set([rope[9]])

di = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

for line in f.readlines():
    d, num = line.split()
    num = int(num)

    for _ in range(num):
        rope[0] = (rope[0][0] + di[d][0], rope[0][1] + di[d][1])
        for i in range(1, 10):
            rope[i] = move_knot(rope[i-1], rope[i])
        p1.add(rope[1])
        p2.add(rope[9])


print(f"p1: knot visited {len(p1)} unique places")
print(f"p2: knot visited {len(p2)} unique places")
