x = 1
register = []

f = open("input.txt", "r")

# p1
for line in f.readlines():
    command = line.strip("\n").split()
    if command[0] == "noop":
        register.append(x)
    elif command[0] == "addx":
        # value changed at END of cycle 2
        register.append(x)
        register.append(x)
        x += int(command[1])

totalSignalStrength = sum([ cycle*register[cycle-1] for cycle in range(20, 221, 40) ])
print(f"p1 signal strength = {totalSignalStrength}")

# p2
for cycle, spriteCenter in enumerate(register):
    # find where sprite center should be
    sprite = [spriteCenter - 1, spriteCenter, spriteCenter + 1]
    # figure out whether pixel should be illuminated or not
    print(end="##" if (cycle%40) in sprite else "  ")
    if ((cycle+1) % 40 == 0): print()

