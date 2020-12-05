import fileinput, math, bisect
filename = "inputs/day5.txt"

def first(x,y):
    return (x, x + math.ceil((y - x) / 2))

def last(x,y):
    return (x + math.ceil((y - x) / 2), y)

directions = {"F": first, "B": last, "L": first, "R": last}

maxseat = 0
def get_seat_id(row, col):
    return row * 8 + col

def binsearch(min, max, attr):
    #print(min, max, attr)
    if len(attr) == 0:
        return min
    else:
        r = directions[attr[0]](min, max)
        return binsearch(r[0], r[1], attr[1:])
seats = []
for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    rowmax = 127
    rowmin = 0
    columnmax = 7
    columnmin = 0
    if len(line_data) < 10:
        continue
    #print(line_data)
    rows = line_data[:-3]
    cols = line_data[-3:]
    r = binsearch(rowmin, rowmax, rows)
    c = binsearch(columnmin, columnmax, cols)
    #print("Row: " + str(r))
    #print("Column: " + str(c))
    seat = get_seat_id(r,c)
    bisect.insort(seats, seat - 80) 
    maxseat = max((maxseat, seat))

myseat = 0
for index, s in enumerate(seats):
    if (index != s):
        myseat = s + 80
        #print(s)
        break

print(maxseat)
print(myseat)
