from copy import deepcopy

data = open("input.txt").read().strip()

monkeys = []
operations = []
tests = []
true = []
false = []

# look for double space to separate monkeys
for monkey in data.split("\n\n"):
    num, items, operation, test, t, f = monkey.split("\n")

    monkeys.append( [int(i) for i in items.split(':')[1].split(',')] )
    operation = ''.join(operation.split()[-3:])
    operations.append(lambda old, operation=operation : eval(operation))
    tests.append(int(test.split()[-1]))
    true.append(int(t.split()[-1]))
    false.append(int(f.split()[-1]))

starting_monkeys = deepcopy(monkeys) # stupid python storing references to variables

# (x+a)%23==0 -> ((x%23)+a)%23 == 0
# (x*a)%23==0 -> ((x%23)*a)%23 == 0
# just keep track of the number modulo
mod = 1
for x in tests:
    mod *= x

for part in [1,2]:
    items_counted = [0 for _ in range(len(monkeys))]
    monkeys = deepcopy(starting_monkeys) # reset monkeys
    for r in range(20 if part == 1 else 10000): # number of rounds
        for monkey in range(len(monkeys)):
            for item in monkeys[monkey]:
                items_counted[monkey] += 1
                new_worry = operations[monkey](item)
                # adjust worry level based on part
                if (part == 1): new_worry = new_worry // 3
                else: new_worry %= mod
                # find out which monkey to throw item to
                if (new_worry % tests[monkey] == 0): monkeys[true[monkey]].append(new_worry)
                else:                                monkeys[false[monkey]].append(new_worry)
            # all items now thrown so empty this monkeys list
            monkeys[monkey] = []
    # sort number of items counted and multiply 2 most busy monkeys to get monkey business
    sorted_counts = sorted(items_counted, reverse=True)
    monkey_business = sorted_counts[0] * sorted_counts[1]
    print(f"monkey business for p{part} = {monkey_business}")


