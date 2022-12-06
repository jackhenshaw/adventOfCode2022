def decodeMessage(string, nLetters):
    # string too short
    if (len(string) < nLetters): return -1
    # create array to store nLetters
    temp = []
    for i, s in enumerate(string):
        if (i < nLetters):
            temp.append(s)
            continue
        else:
            temp[i%nLetters] = s
        # check unique
        if (len(set(temp)) == len(temp)):
            return i+1
    return -1

f = open("input.txt", "r")
dstream = f.readline().strip("\n")
p1 = decodeMessage(dstream,  4) #  4 letters for start of packet
p2 = decodeMessage(dstream, 14) # 14 letters for start of message
print(f"p1 = {p1}")
print(f"p2 = {p2}")
