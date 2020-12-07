import fileinput

l = []
for line in fileinput.input(files=('inputs/day1.txt')):
    l.append(int(line))

for i, x in enumerate(l, start=0):
    looking = 2020 - x
    for j, y in enumerate(l[i:], start=i):

        if looking == y:
            print("Part 1: " + str(looking * x))

        looking2 = looking - y
        for z in l[j:]:
            if looking2 == z:
                print("Part 2: " + str(looking2 * x * y))

