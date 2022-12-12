calories = []
cal = 0
with open("input.txt", "r") as fin:
    for line in fin:
        line = line.strip("\n")
        if (line == ""):
            calories.append(cal)
            cal = 0
        else:
            cal += float(line)

calories.sort(reverse=True)
print(f"Top 3 elves: {calories[0]:.0f} {calories[1]:.0f} {calories[2]:.0f}")
print(f"with sum = {calories[0]+calories[1]+calories[2]:.0f}")
