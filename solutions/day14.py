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


#address bitwise
def put2(memory, addr, value, masks):
    if len(masks) == 0:
        memory[addr] = value
        return
    curr = masks[-1]
    if (curr[1] == "X"):
        put2(memory, addr, value, masks[:-1])
        put2(memory, addr ^ curr[0], value, masks[:-1])
    if (curr[1] == 1):
        addr = addr | curr[0]
    # if (curr[1] == 0): #ignore 0 now
    put2(memory, addr, value, masks[:-1])


def create_masks(maskline):
    mask = []
    for x in maskline:
        if x == "X":
            mask.append("X")
        else:
            mask.append(int(x))
    masks = []
    size = len(mask) - 1
    for i, x in enumerate(mask):
        masks.append((pow(2, size-i), x))
    return masks

masks = [None for x in range(36)]
memory = {}
memory2 = {}
for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    split = line_data.split(" = ")
    if (split[0] == "mask"):
        maskline = split[1].strip()
        masks = create_masks(maskline)
    else:
        l = line_data.split("=")
        addr = int(split[0].strip().split("[")[1].split("]")[0])
        value = int(split[1].strip())
        put(memory, addr, value, masks)
        put2(memory2, addr, value, masks)
#print(memory)
print("Part 1: ", sum(memory.values()))

print()    
print("Part 2: ", sum(memory2.values()))
