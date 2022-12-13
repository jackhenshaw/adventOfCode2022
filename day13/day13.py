from functools import cmp_to_key

def compare(l, r):
    if ( isinstance(l, int) and isinstance(r, int) ):
        if l < r: return -1
        elif l == r: return 0
        else: return 1
    elif ( isinstance(l, list) and isinstance(r, list) ):
        i = 0
        while i < len(l) and i < len(r):
            c = compare(l[i], r[i])
            if c == -1:
                return -1
            elif c == 1:
                return 1
            i += 1
        if i==len(l) and i < len(r):
            return -1
        elif i == len(r) and i < len(l):
            return 1
        else:
            return 0
    elif ( isinstance(l, int) and isinstance(r, list) ):
        return compare([l], r)
    elif ( isinstance(l, list) and isinstance(r, int) ):
        return compare(l, [r])
    else:
        print("ahhh broken")

data = open("input.txt").read().strip()

right_order = []
packets     = [] # needed for p2
for pair in data.split("\n\n"):
    left, right = [eval(x) for x in pair.split("\n")]
    right_order.append(compare(left, right))
    # needed for p2
    packets.append(left)
    packets.append(right)

right_order = [i+1 for i in range(len(right_order)) if right_order[i] == -1]
print(f"p1 = {sum(right_order)}")

# add the divider packets to list of packets
packets.append([[2]])
packets.append([[6]])
# sort using lambda function of our custom comparison function
packets = sorted(packets, key=cmp_to_key(lambda left, right: compare(left,right)))
decoder_key = 1
# probably more efficient ways of finding these two elements
for i, packet in enumerate(packets):
    if (packet==[[2]] or packet==[[6]]):
        decoder_key *= i+1
print(f"p2 = {decoder_key}")
