import fileinput, math
import functools
filename = "inputs/day12.txt"

eastwest = 0
northsouth = 0

rotation = ['N', 'E', 'S', 'W']
directions = {'N': 0, 'E': 0,'S': 0,'W': 0 }
front = 'E'
#Assumes rotation only in increments of 90 degress
def rotate(dir, unit):
    global front
    i = rotation.index(front)
    c = unit // 90
    if dir == "R":
        #rotate right
        i = (i + c) % 4 # reset back
    if dir == "L":
        i -= c
    front = rotation[i]

def move(dir, unit):
    if dir == "R" or dir == "L":
        rotate(dir, unit)
    elif dir == "F":
        directions[front] += unit
    else:
        directions[dir] += unit
for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    if len(line_data) == 0:
        continue
    dir = line_data[:1]
    unit = int(line_data[1:])
    move(dir, unit)

ew  = abs(directions['E'] - directions['W'])
ns = abs(directions['N'] - directions['S'])
#print(directions)
print("Part 1: " + str(ew + ns))


rotation = ['N', 'E', 'S', 'W']
waypoint  = [1, 10, 0, 0]
directions = {'N': 0, 'E': 0,'S': 0,'W': 0 }
# F
def move_to_waypoint(unit):
    for i, n in enumerate(waypoint):
        key = rotation[i]
        directions[key] += n * unit

def move_waypoint_dir(f, b, unit):
    print(waypoint)
    print("moving", unit, "toward", f, "away from", b)
    v = waypoint[b]
    # add to east or remove from west
    if waypoint[b] == 0:
        waypoint[f] += unit
    else:
        new_v = v - unit
        if new_v < 0:
            waypoint[f] = abs(new_v)
            waypoint[b] = 0
        else:
            waypoint[b] = new_v
    print(waypoint)

# NSEW
def move_waypoint(dir, unit):
    if dir == "E":
        move_waypoint_dir(1,3, unit)
    if dir == "N":
        move_waypoint_dir(0,2, unit)
    if dir == "W":
        move_waypoint_dir(3,1, unit)
    if dir == "S":
        move_waypoint_dir(2,0, unit)

def swap(waypoint, i, j):
    waypoint[i] = waypoint[j]
    
# RL
def rotate_waypoint(dir, unit):
    c = unit // 90
    global waypoint
    print(waypoint)
    print("Rotating", dir, c)
    if dir == "R":
        waypoint = waypoint[-c:] + waypoint[:-c]
    if dir == "L":
        waypoint = waypoint[c % 4:] + waypoint[:c % 4]
    print(waypoint)

def move2(dir, unit):
    if dir == "R" or dir == "L":
        rotate_waypoint(dir, unit)
    elif dir == "F":
        move_to_waypoint(unit)
    else:
        move_waypoint(dir, unit)

for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    if len(line_data) == 0:
        continue
    dir = line_data[:1]
    unit = int(line_data[1:])
    move2(dir, unit)
    print()

ew  = abs(directions['E'] - directions['W'])
ns = abs(directions['N'] - directions['S'])
print(directions, waypoint)
print("Part 2: " + str(ew+ns))
