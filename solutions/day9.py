import fileinput, math, bisect
import functools
filename = "inputs/day9.txt"

slice_size = 25 #5 for example input, 25 for real input

def is_summable(answer, sublist):
    for i, x in enumerate(sublist[:-1]):
        for y in sublist[i+1:]:
            #print (x, y, x+y)
            if x + y == answer:
                return True
    return False

def get_summable_range(answer, sublist):
    for i, x in enumerate(sublist):
        last = is_summable_rec(answer, i+1, sublist, x)
        if last is not None:
            return sublist[i:last]
    return sublist
def is_summable_rec(answer, index, sublist, curr):
    if (curr == answer):
        return index
    if (curr > answer):
        return None
    
    val = sublist[index]
    return is_summable_rec(answer,index + 1, sublist, curr + val)


def find_min_max(sublist):
    mn = sublist[0]
    mx = sublist[0]
    for x in sublist:
        mn = min(mn, x)
        mx = max(mx, x)
    return (mn, mx)

preamble = []

for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    if len(line_data) == 0:
        break
    test = int(line_data)

    total_length = len(preamble)
    
    if total_length < slice_size: # Last index is test
        preamble.append(test)
        #skip until we have enough for the preamble
        continue
    
    sublist = preamble[(total_length) - slice_size:] #slice a list of size slice_size
    print("Testing :" + line_data)

    if not is_summable(test, sublist):
        print("Part 1: " + line_data)
        # now go through and expand of above 
        rg = get_summable_range(test, preamble)
        minmax = find_min_max(rg)
        print("Part 1: " + str(minmax[0] + minmax[1]))
        break
    preamble.append(test)