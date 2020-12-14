import fileinput, bisect
import numpy as np
filename = "inputs/day13.txt"

with open(filename) as fp: 
    line_data = fp.readline().strip()
    id = int(line_data)
    line_data = fp.readline().strip()
    schedule = line_data.split(",")
    schedule2 = list(filter(lambda x: not x == "x", schedule))
    # Find the multiple of the list values closest but not under id
    modulos = list(map(lambda x: (int(x) * ((id // int(x)) + 1)) % id, schedule2))
    lowest = 0
    for i, x in enumerate(modulos):
        if min(x, modulos[lowest]) == x:
            lowest = i
    
    # print(lowest)
    # print(modulos)
    # print(schedule)
    print("Part 1: " + str(modulos[lowest] * int(schedule2[lowest])))



def find_match_rc(t, diff, b2, incr):
    while (not ((t + diff) % b2 == 0)) or (t == 0):
        t += incr
    return t

def find_matches(schedule):
    #find the largest number 
    high = 0
    low = int(schedule[0])
    low_ind = 0
    index = 0
    # Find the highest and lowest
    for i, x in enumerate(schedule):
        if x == "x":
            continue
        v= int(x)
        high = max(high, v)
        low = min(low, v)
        if high == v:
            index = i
        if low == v:
            low_ind = i
    first = 0
    works = False

    first = find_match_rc(high, low, high, -(index - low_ind))
    skip = high * low
    c = 0
    while not works:
        works = True
        for i, x in enumerate(schedule):
            if x == "x":
                continue
            diff = -(index - i)
            #print("Testing", first, diff, x)
            if (first + diff) % int(x) == 0:
                works = True
            else:
                first += skip
                c +=1
                works = False
                #
                break
    print("Took", c, "iterations")
    return first - index

def run(schedule):
    s = list(map(lambda x: (x[0],int(x[1])), list(filter(lambda x: not x[1] == "x", enumerate(schedule)))))
    #print(s)
    t = 0
    incr = 1
    
    for i, b in s:
        t = find_match_rc(t, i, b, incr)
        incr = b * incr
        #print (t)
    return t
# for line in fileinput.input(files=("inputs/day13p2_ex.txt")):
#     line_data = line.strip()
#     s = line_data.split(",")
#     #print(line_data)
#     #print(run(s))
#     #print()

print("Part 2: " + str(run(schedule)))
