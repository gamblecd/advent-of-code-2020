import fileinput, copy
import functools
filename = "inputs/day11.txt"
occupied = '#'
empty = 'L'


def build_seats(file, arr=[]):
    for line in fileinput.input(files=(file)):
        line_data = line.strip()
        length = len(line_data)
        if length != 0:
            l = []
            for i in range(len(line_data)):
                l.append(line_data[i])
            arr.append(l)
    return arr

beginning_seats = build_seats(filename, []);
ex1 = build_seats("inputs/day11p2_ex1.txt", [])
ex2 = build_seats("inputs/day11p2_ex2.txt", [])
ex3 = build_seats("inputs/day11p2_ex3.txt", [])

def is_seat(char):
    return char == "L" or char == "#"

def find_seat(direction, row, col, seats, depth):
    if direction == (0, 0):
        return "."
    x = row + direction[0]
    y = col + direction[1]
    # print(x,y)
    # print(seats[x][y])
    if x < 0 or x >= len(seats):
        return "."
    if y < 0 or y >= len(seats[x]):
        return "."
    if (is_seat(seats[x][y])):
        return seats[x][y]
    else :
        if (depth == 1):
            return  "."
        else:
            return find_seat(direction, x, y, seats, depth)

def count_surrounding_seats(row, col, seats, depth = 1):
    directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    around = []
    for x in directions:
        #print("choosing direction " + str(x))
        around.append(find_seat(x, row, col, seats, depth))
    #print(around)
    return len(list(filter(lambda x: x == occupied, around)))

def vacate_rule(row, col, seats, data):
    def apply(seat_count_provider):
        occ_count = seat_count_provider(row, col, seats)
        if occ_count >= 4:
            data[row][col] = empty
            return 1
        return 0
    return apply

def vacate_rule2(row, col, seats, data):
    def apply(seat_count_provider):
        occ_count = seat_count_provider(row, col, seats, 0)
        if occ_count >= 5:
            data[row][col] = empty
            return 1
        return 0
    return apply

def fill_rule(row, col, seats, data,):
    def apply(seat_count_provider):
        occ_count = seat_count_provider(row, col, seats)
        if occ_count == 0:
            data[row][col] = occupied
            return 1
        return 0
    return apply

def fill_rule2(row, col, seats, data,):
    def apply(seat_count_provider):
        occ_count = seat_count_provider(row, col, seats, 0)
        if occ_count == 0:
            data[row][col] = occupied
            return 1
        return 0
    return apply


def apply_rule(rule, seat_count_provider):
    return rule(seat_count_provider)

def apply_rules2(row, col, seats, data):
    curr_seat = seats[row][col]
    if curr_seat == empty:
        return apply_rule(fill_rule2(row, col, seats, data), count_surrounding_seats)
    elif curr_seat == occupied:
        return apply_rule(vacate_rule2(row, col, seats, data), count_surrounding_seats)
    return 0

def apply_rules(row, col, seats, data):
    curr_seat = seats[row][col]
    if curr_seat == empty:
        return apply_rule(fill_rule(row, col, seats, data), count_surrounding_seats)
    elif curr_seat == occupied:
        return apply_rule(vacate_rule(row, col, seats, data), count_surrounding_seats)
    return 0

def apply_rules_to_all(seats, rules_apply):
    mod_count = 0
    #print_seats(seats)
    data = copy.deepcopy(seats)

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            mod_count += rules_apply(i, j, seats, data)
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
c = 0
while(total_mod_count != 0):
    #print("Step " + str(c))
    data, total_mod_count = apply_rules_to_all(data, apply_rules)
    c += 1

print("Part 1: " + str(count_occupied_seats(data)))
print(str(c) + " passes to resolve")

# For some reason part 2 doesn't work if part 1 is run
data = copy.deepcopy(beginning_seats)
c = 0
total_mod_count = 1
while(total_mod_count != 0):
    #print("Step " + str(c))
    data, total_mod_count = apply_rules_to_all(data, apply_rules2)
    c += 1

print("Part 2: " + str(count_occupied_seats(data)))
print(str(c) + " passes to resolve")
