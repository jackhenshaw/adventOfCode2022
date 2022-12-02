

calories = []
cal = 0
with open("input2.txt", "r") as fin:
    for line in fin:
        line = line.strip("\n")
        if (line == ""):
            calories.append(cal)
            cal = 0
        else:
            cal += float(line)

calories.sort(reverse=True)
print(f"max calories = {calories[0]}")
print(f"Top 3: {calories[0]} {calories[1]} {calories[2]}")
print(calories[0]+calories[1]+calories[2])
