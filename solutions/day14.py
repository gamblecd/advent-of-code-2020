import fileinput, bisect
import functools
filename = "inputs/day14.txt"

def put(memory, addr, value, masks):
    for x in masks:
        if (x[1] == 1):
            value = value | x[0]
        if (x[1] == 0):
            value= value & ~(x[0])
    memory[addr] = value

def create_masks(maskline):
    mask = []
    for x in maskline:
        if x == "X":
            mask.append(None)
        else:
            mask.append(int(x))
    masks = []
    size = len(mask) - 1
    for i, x in enumerate(mask):
        if not x is None:
            masks.append((pow(2, size-i), x))
    return masks

masks = [None for x in range(36)]
memory = {}
for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    split = line_data.split(" = ")
    if (split[0] == "mask"):
        maskline = split[1].strip()
        masks = create_masks(maskline)
        print(masks)
    else:
        l = line_data.split("=")
        addr = int(split[0].strip().split("[")[1].split("]")[0])
        value = int(split[1].strip())
        put(memory, addr, value, masks)

print(memory)
print("Part 1: ", sum(memory.values()))

print()    
print("Part 2: " + str())
