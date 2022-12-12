with open("input.txt") as f:
    ans_p1 = ans_p2 = 0

    for line in f:
        opp, me = line.split()
        # convert letters to numbers
        opp = "ABC".index(opp)
        me  = "XYZ".index(me)

        # (p1) add score for what you played
        ans_p1 += me + 1

        # (p1) find out if win/loss/draw
        match (me-opp) % 3:
            case 0: # draw
                ans_p1 += 3
            case 1: # win
                ans_p1 += 6
            case 2: # loss
                ans_p1 += 0

        # (p2) from outcome, work out shape played (and add outcome)
        match me:
            case 0: # lose
                ans_p2 += (opp - 1)%3 + 1
            case 1: # draw
                ans_p2 += opp + 1
                ans_p2 += 3
            case 2: # win
                ans_p2 += (opp + 1)%3 + 1
                ans_p2 += 6

print(f"part 1 = {ans_p1}")
print(f"part 2 = {ans_p2}")

