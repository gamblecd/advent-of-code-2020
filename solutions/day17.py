import fileinput, numpy as np
import copy
filename = "inputs/day17.txt"

for line in fileinput.input(files=(filename)):
    line_data = line.strip()

def is_active(char):
    return char == "#"

def find_cube(direction, coord, cubes):
    if len(list(filter(lambda x: x != 0, direction))) == 0:
        return False
    new_coord = [coord[i] + direction[i] for i in range(len(direction))]
    cell_val = get_cell(cubes, new_coord)
    return is_active(cell_val)

def find_cube_old(direction, row, col, hgt, cubes, depth=1):
    if direction == (0, 0, 0):
        return "."
    x = row + direction[0]
    y = col + direction[1]
    z = hgt + direction[2]
    # print(x,y)
    # print(seats[x][y])
    if x < 0 or x >= len(cubes):
        return "."
    if y < 0 or y >= len(cubes[x]):
        return "."
    if z < 0 or z >= len(cubes[x][y]):
        return "."
    if (is_active(cubes[x][y][z])):
        return cubes[x][y][z]
    else :
        return  "."

def get_dimensions(cubes):
    curr = cubes
    ds = []
    while type(curr) is list:
        ds.append(len(curr))
        curr = curr[0]
    return ds

def find_surrounding_active_rec(cubes, surr, direction, coord):
    d = len(direction)
    if d == len(coord):
        surr.append(find_cube(direction, coord, cubes))
    else:
        opts = (-1, 0, 1)
        for i in opts:
            find_surrounding_active_rec(cubes, surr, direction + (i,), coord )

def find_surrounding_active_ds(cubes, coord):
    ds = get_dimensions(cubes)
    opts = (-1, 0, 1)
    surr = []
    find_surrounding_active_rec(cubes, surr, (), coord)
    count = len(list(filter(lambda x: x, surr)))
    return count

    
def find_surrounding_active(cubes, x,y,z):
    opts = (-1, 0, 1)
    surr = []
    for x_d in opts:
        for y_d in opts:
            for z_d in opts:
                dir = (x_d,y_d,z_d)
                surr.append(find_cube(dir, (x, y, z), cubes))
                #surr.append(find_cube_old(dir, x, y, z, cubes))
    count = len(list(filter(lambda x: x, surr)))
    return count



# TODO RE DO PRint 
def print_cube(cubes):
    hght = len(cubes[0][0])
    for layer in range(hght):
        print("z=", layer - origin[2])
        for x in cubes:
            for y in x:
                print(y[layer], end='')
            print()
        print()
#print(origin)
#print_cube(cubes)

def get_cell(cubes, coord):
    curr = cubes
    for x in coord:
        if x < 0 or x >= len(curr):
            return "."
        curr = curr[x]
    return curr

def copy_cell_for_expanse(cubes, coord):
    curr = cubes
    for i in range(len(coord)):
        c = coord[i]
        if c == 0 or c > len(curr):
            return "."
        curr = curr[0]
    return get_cell(cubes, list(map(lambda c: c-1, coord)))
    if x == 0 or x > len(cubes):
        return "."
    if y == 0 or y > len(cubes[0]): 
        return "."
    if z == 0 or z > len(cubes[0][0]):
        return "."
    else:
        return cubes[x-1][y-1][z-1]

def create_dimension(cubes, dimensions, coord):
    if len(dimensions) == 0:
        return copy_cell_for_expanse(cubes, coord)
        # put cell_value in curr at coord
        curr[coord[-1]] = cell_value
    else:
        curr_dim = []
        for i in range(dimensions[0]):
            cell_value = create_dimension(cubes, dimensions[1:], coord + (i,))
            curr_dim.append(cell_value)
        return curr_dim

def expand(cubes):
    curr = cubes
    # Get the dimensions and expand by 2 in every direction
    ds = list(map(lambda x: x+2, get_dimensions(cubes)))

    new_origin = [ds[i] // 2 for i in range(len(ds))]

    cubes = create_dimension(cubes, ds, ())

    # cubes = [
    #             [
    #                 [
    #                     copy_cell_for_expanse(cubes, k, j, i) 
    #                     for i in range(z)
    #                 ] for j in range(y)
    #             ] for k in range(x)
    #         ]
    return cubes, new_origin

# for i in range(6):
# increase in all directions
#print(origin)
def apply_rules(cubes, coord):
    count = find_surrounding_active_ds(cubes, coord)
    active_cube = is_active(get_cell(cubes, coord))
    if active_cube and not (count == 2 or count == 3):
        return False
        #deactivate
    elif (not active_cube) and count == 3:
        #activate
        return True
    return active_cube


def sum_active(cubes):
    if not type(cubes) is list:
        if (is_active(cubes)):
            return 1
        else:
            return 0
    else:
        c = 0
        for i in cubes:
            c += sum_active(i)
        return c

def sum_active_old(cubes):
    c = 0
    for x in range(len(cubes)):
        for y in range(len(cubes[0])):
            for z in range(len(cubes[0][0])):
                if is_active(cubes[x][y][z]):
                    c += 1
    return c

def set_cell(cubes, coord, value):
    curr = cubes
    for x in coord[:-1]:
        curr = curr[x]
    curr[coord[-1]] = value

def apply_to_all(cubes, next_cubes, curr, coord):
    if not type(curr) is list:
        cell_val = "."
        if (apply_rules(cubes, coord)):
            cell_val = '#'
        set_cell(next_cubes, coord, cell_val)
    else:
        for i, x in enumerate(curr):
            apply_to_all(cubes, next_cubes, x, coord + (i,))


def run(cubes):
    for i in range(6):
        cubes, origin = expand(cubes)
        next_cubes = copy.deepcopy(cubes)
        #print_cube(next_cubes)
        apply_to_all(cubes, next_cubes, cubes, ())
        cubes = next_cubes
        #print_cube(cubes)
    return sum_active(cubes)

lines = []
for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    length = len(line_data)
    if length != 0:
        lines.append(line_data)

def create_3d_cubes(lines):
    cubes = []
    for line in lines:
        l = []
        for i in range(len(line)):
            l.append([line[i]])
        cubes.append(l)
    return cubes

def create_4d_cubes(lines):
    cubes = []
    for line in lines:
        l = []
        for i in range(len(line)):
            l.append([[line[i]]])
        cubes.append(l)
    return cubes

print("Part 1: ", run(create_3d_cubes(lines)))
print()
print("Part 2: ", run(create_4d_cubes(lines)))
