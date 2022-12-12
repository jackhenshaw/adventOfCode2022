from collections import defaultdict, OrderedDict

f = open("input.txt", "r")

sizes = defaultdict(int) # used to store size of each directory with full path
path = [] # used to keep track of absolute path to current directory

for line in f.readlines():
    if line.startswith("$ cd"):
        dirName = line.split()[-1]
        if dirName == "..":
            path.pop() # go back up a directory
        else:
            path.append(dirName) # go into directory
    elif line.startswith("$ ls"):
        continue # ignore as does not change anything
    else:
        # listing files/directories
        size, fileName = line.split()
        if (size.isdigit()):
            for i in range(len(path)):
                sizes['/'.join(path[:i+1])] += int(size)

p1 = sum([value for key, value in sizes.items() if value <= 100000])
print(f"p1 = {p1}")

sorted_dirs = {k: v for k, v in sorted(sizes.items(), key=lambda item: item[1])}

free_space = 70000000 - sorted_dirs['/']
deleteSize = 30000000 - free_space

for key, value in sorted_dirs.items():
    if (value < deleteSize):
        continue
    print(f"part2: {key} {value}")
    break
