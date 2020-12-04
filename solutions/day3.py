import fileinput
l = [];

slopes = [(1,1), (3,1), (5, 1), (7,1), (1, 2)]

def check_slope_for_trees(x, y):
    sled_pos = (0, 0)
    tree_count = 0
    for index, line in enumerate(l, start=0):
        if not (index % y == 0):
            continue
        pattern_size = len(line)
        #print(line)
        i = (sled_pos[0] % (pattern_size));
        #print(pattern_size, sled_pos[0], i)
        
        tree = line[i] == "#";
        if tree:
            tree_count = tree_count + 1;
            line = line[:i] + 'X' + line[i+1:]
        else:
            line = line[:i] + 'O' + line[i+1:]
        #print(line)
        sled_pos = (sled_pos[0] + x, sled_pos[1] + y);
    return tree_count;

sled_pos = (0, 0)
sled_x = 3
sled_y = 1
tree_count = 0;
for line in fileinput.input(files=('inputs/day3.txt')):
    l.append(line.strip())

count = 1
for slope in slopes:
    tc = check_slope_for_trees(slope[0], slope[1]);
    print(tc)
    count = count * tc

# check_slope_for_trees(7, 1);
print(count)