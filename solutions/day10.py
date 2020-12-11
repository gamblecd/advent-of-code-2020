import fileinput, bisect
import functools
filename = "inputs/day10.txt"

adapters =[]
for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    j = int(line_data)
    bisect.insort(adapters, j)


counts = [0,0,0, 1] # 1,2, or 3 jolts difference, 3 starts higher because of built in adapter

def save_separation(last, curr):
    counts[curr-last] += 1
    return curr


def count_separation(l):
    functools.reduce(save_separation, l, 0)

def compare_index(l, curr, j):
    le = len(l)
    if (j >= le):
        return 0
    n = l[j] - curr
    if n > 3:
        return 0
    if n <= 3:
        return 1

def count_total_possible_separations(l):
    s = [0 for i in range(len(l))]
    curr = 0
    for i, x in enumerate(l[:-1]): #last one is always only three
        n = l[i] - curr
        #print(l[1], curr, n)

        if n == 3:
            s[i] = 1 # No other options
        if n == 2:
            s[i] = 1 + compare_index(l, curr, i + 1)
            # Check the next index for a diff of three
        if n == 1:
            s[i] = 1 + compare_index(l, curr, i + 1) + compare_index(l, curr, i + 2)
            # Check the next two indices for a diff of 2 and 3
        curr = x       

    s[-1] = 1 # Last one is always 3
    return s

def find_paths(s, i, memo):
    if i == len(s):
        return 1
    v = s[i]
    r = memo[i]
    if r == 0:
        if v == 1:
            r = find_paths(s, i + 1, memo)
        if (v==2):
            r = find_paths(s, i +1, memo) + find_paths(s, i+2, memo)
        if (v==3):
            r = find_paths(s, i +1, memo) + find_paths(s, i+2, memo) + find_paths(s, i+3,memo)
        memo[i] = r
    return r
print(adapters)
count_separation(adapters)
print("Part 1: " + str(counts[1] * counts[3]))

paths = count_total_possible_separations(adapters)
memo = [0 for x in range(len(paths))]
print(paths)
print(find_paths(paths,0, memo))
print(memo)
