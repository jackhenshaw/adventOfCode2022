import re
from collections import deque

f = open("input.txt", "r")

crates, instructions = f.read().split("\n\n")

# create stacks to hold information
stacks = []
for line in crates.splitlines():
    # want to read in chunks of 4's
    for i, index in enumerate(range(1, len(line), 4)):
        # make enough stacks to hold all crates
        while i >= len(stacks):
            stacks.append(deque())
        # if crate exists, add to stack
        if (line[index] != " " and not line[index].isnumeric()):
            stacks[i].append(line[index])

for s in stacks:
    print(s)

for command in instructions.splitlines():
    numToMove, stackFrom, stackTo = map(int, re.findall('[0-9]+', command))
    for i in range(numToMove):
        stacks[stackTo-1].appendleft(stacks[stackFrom-1].popleft())

# top of the stacks
p1 = "".join(s[0] for s in stacks)
print(p1)

# part 2
f = open("input.txt", "r")

crates, instructions = f.read().split("\n\n")

# create stacks to hold information
stacks = []
for line in crates.splitlines():
    # want to read in chunks of 4's
    for i, index in enumerate(range(1, len(line), 4)):
        # make enough stacks to hold all crates
        while i >= len(stacks):
            stacks.append(deque())
        # if crate exists, add to stack
        if (line[index] != " " and not line[index].isnumeric()):
            stacks[i].append(line[index])

i = 0
for command in instructions.splitlines():
    numToMove, stackFrom, stackTo = map(int, re.findall('[0-9]+', command))
    # temp array to store crates in correct order
    temp = []
    for i in range(numToMove):
        temp.append(stacks[stackFrom-1].popleft())
    # adding crates to the new stack as a whole
    for i in range(len(temp)):
        stacks[stackTo-1].appendleft(temp[len(temp)-i-1])

# top of the stacks
p2 = "".join(s[0] for s in stacks)
print(p2)

