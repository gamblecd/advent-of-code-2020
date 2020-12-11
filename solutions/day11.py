import fileinput, copy
import functools
filename = "inputs/day11.txt"
occupied = '#'
empty = 'L'

beginning_seats = []
for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    length = len(line_data)
    if length != 0:
        l = []
        for i in range(len(line_data)):
            l.append(line_data[i])
        beginning_seats.append(l)


# Returns a list of the nine points with [4] being (row, col) and the first three being the first row
# Probably a more succint way of doing this but who cares
def get_surrounding_seats(row, col, seats):
    row_length = len(seats[row])
    col_length = len(seats)
    surround = ['.' for x in range(9)]
    rm = row - 1
    cm = col - 1
    rp = row + 1
    cp = col + 1
    # Row before
    if rm >= 0:
        if cm >= 0:
            surround[0] = seats[rm][cm]
        surround[1] = seats[rm][col]
        if cp < row_length:
            surround[2] = seats[rm][cp]
    #Current Row
    if cm >= 0:
        surround[3] = seats[row][cm]
    surround[4] = seats[row][col]
    if cp < row_length:
        surround[5] = seats[row][cp]
    # Last Row
    if rp < col_length:
        if cm >= 0:
            surround[6] = seats[rp][cm]
        surround[7] = seats[rp][col]
        if cp < row_length:
            surround[8] = seats[rp][cp]
    return surround

def vacate_if_too_many_seats(row, col, seats, data):
    arround = get_surrounding_seats(row, col, seats)
    #ignore [4]
    #arround.pop(4)
    # print(row, col)
    # print(seats[row-1])
    # print(seats[row])
    # print(seats[row+1])
    # print(arround)
    occ_count = len(list(filter(lambda x: x == occupied, arround)))
    if occ_count > 4:
        data[row][col] = empty
        return 1
    return 0

def fill_if_no_occupied_seats(row, col, seats, data):
    arround = get_surrounding_seats(row, col, seats)
    #ignore [4]
    arround.pop(4)
    occ_count = len(list(filter(lambda x: x == occupied, arround)))
    if occ_count == 0:
        data[row][col] = occupied
        return 1
    return 0

def apply_rules(row, col, seats, data):
    curr_seat = seats[row][col]
    if curr_seat == empty:
        return fill_if_no_occupied_seats(row, col, seats, data)
    elif curr_seat == occupied:
        return vacate_if_too_many_seats(row, col, seats, data)
    return 0
def apply_rules_to_all(seats):
    mod_count = 0
    #print_seats(seats)
    data = copy.deepcopy(seats)

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            mod_count += apply_rules(i, j, seats, data)
    #print_seats(data)

    return (data, mod_count)

def count_occupied_seats(seats):
    occupied_count = 0
    for x in seats:
        for y in x:
            if y == occupied:
                occupied_count += 1
    return occupied_count

total_mod_count = 1

def print_seats(seats):
    for x in seats:
        print("".join(x))
    print()


data = copy.deepcopy(beginning_seats)
#print_seats(data)
c = 1
while(total_mod_count != 0):
    #print("Step " + str(c))
    data, total_mod_count = apply_rules_to_all(data)
    c += 1
    #print_seats(data)

print("Part 1: " + str(count_occupied_seats(data)))
