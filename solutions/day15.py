import fileinput
filename = "inputs/day15_ex.txt"

def play_turn(turn, number, indices):
    #print(arr, number)
    index = indices[number]
    z = turn - 1
    x = 0
    if not index is None:
        x = z - index
    indices[number] = z
    return x

for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    t = 30000000
    indices = [None for x in range(t)]
    l = 0
    last = 0
    for i, x in enumerate(list(map(int, line.split(",")))):
        indices[x] = i
        last = x
        l += 1
    init_turns = l 
    turn_diff = init_turns + 1
    #print(arr)
    for x in range(t-init_turns):
        last = play_turn(x + init_turns, last, indices)
        #print(last)
        if x+turn_diff == 2020:
            print("Part 1: ", last)
        #if (arr[-1] == 0):
            #print(x+(len(arr)))
    #print(arr)
    print()
    print("Part 2: ", last)
