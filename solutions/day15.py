import fileinput, bisect
import functools
filename = "inputs/day15_ex.txt"

def init_game(line):
    arr = list(map(int, line.split(",")))
    return arr

def update_indices(indices, number, new_index):
    index = indices.get(number)
    if index is None:
        indices[number] = [new_index]
    else:
        indices[number] = [new_index, index[0]]

def play_turn(arr, number, indices):
    #print(arr, number)
    index = indices[number]
    z = len(arr)
    x = 0
    if len(index) == 1:
        x = 0
    else:
        last, s_last =  index
        x = last - s_last
    update_indices(indices, x, z)
    arr.append(x)

for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    arr = init_game(line_data)
    indices = {}
    for i, x in enumerate(arr):
        indices[x] = [i]
    t = 30000000
    init_turns = len(arr)
    turn_diff = init_turns + 1
    #print(arr)
    for x in range(t-init_turns):
        play_turn(arr, arr[-1], indices)
        if x+turn_diff == 2020:
            print("Part 1: ", arr[-1])
        #if (arr[-1] == 0):
            #print(x+(len(arr)))
    #print(arr)
    print()
    print("Part 2: ", arr[-1])
