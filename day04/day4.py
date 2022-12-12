import numpy as np

data = np.loadtxt("input.txt", delimiter=',', dtype='str')

p1 = 0
p2 = 0
for d in data:
    # split each element by dashes
    elf1_start, elf1_end = d[0].split('-')
    elf2_start, elf2_end = d[1].split('-')

    elf1_start = int(elf1_start)
    elf1_end   = int(elf1_end)
    elf2_start = int(elf2_start)
    elf2_end   = int(elf2_end)

    elf1 = set(range(elf1_start, elf1_end+1)) if (elf1_start != elf1_end) else {elf1_start}
    elf2 = set(range(elf2_start, elf2_end+1)) if (elf2_start != elf2_end) else {elf2_start}

    # Check if one list fully contained in the other
    if ((elf1_start <= elf2_start <= elf2_end <= elf1_end) or
        (elf2_start <= elf1_start <= elf1_end <= elf2_end)):
        p1 += 1

    # Check for any overlap whatsoever
    if (elf1 & elf2):
        p2 += 1

print(f"p1: {p1}")
print(f"p2: {p2}")
