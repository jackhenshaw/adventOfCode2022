alphabet  = "abcdefghijklmnopqrstuvwxyz"
alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

itemPriority  = 0
badgePriority = 0

# read file and split into list of rucksacks
f = open("input.txt", "r")
rucksacks = [d.strip("\n") for d in f.readlines()]

for i, r in enumerate(rucksacks):
    # part 1: items
    item = set(r[:int(0.5*len(r))]) & set(r[int(0.5*len(r)):])
    itemPriority += alphabet.index(item.pop()) + 1

    # part 2: badges
    if (i%3 != 0): continue
    badge = set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2])
    badgePriority += alphabet.index(badge.pop()) + 1

print(f"p1: items priority = {itemPriority}")
print(f"p2: badge priority = {badgePriority}")
