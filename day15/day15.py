import re

def valid(x,y,S):
    for (sx,sy,d) in S:
        dxy = abs(x-sx)+abs(y-sy)
        if dxy<=d:
            return False
    return True


data = open("input.txt").read().strip()
lines = [line for line in data.split("\n")]

y_test = 2000000
beacons_x = set()         # beacons x position if on test line
unavailable_spots = set() # unavailable spots for beacon on test line
sensor_distance = set()   # list of sensors with distance

for line in lines:
    sensor_x, sensor_y, beacon_x, beacon_y = list(map(int, re.findall('-?[0-9]+', line)))
    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    sensor_distance.add((sensor_x, sensor_y, distance))

    # if beacon on test line, add it to set
    if beacon_y == y_test:
        beacons_x.add(beacon_x)

    # find any spaces on test line that have been "checked"
    distance -= abs(y_test - sensor_y)
    for i in range(sensor_x - distance, sensor_x + distance + 1):
        unavailable_spots.add(i)

# check difference between spots hit by other searches and those that have beacons
p1 = len(unavailable_spots - beacons_x)
print(f"p1 = {p1}")


n_checked = 0
# If there is only one possible position for another beacon, it *must* be distance d+1 from some beacon
# If not, we could find an adjacent position that is possible.
for (sx,sy,d) in sensor_distance:
    # check all points that are d+1 away from (sx,sy)
    for dx in range(d+2):
        dy = (d+1)-dx
        for signx,signy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            n_checked += 1
            x = sx+(dx*signx)
            y = sy+(dy*signy)
            if not(0<=x<=4000000 and 0<=y<=4000000):
                continue
            assert abs(x-sx)+abs(y-sy)==d+1
            if valid(x,y,sensor_distance):
                print(f"p2: {x*4000000 + y}")
                exit()
