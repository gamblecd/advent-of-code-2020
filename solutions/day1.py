import fileinput

l = [];
for line in fileinput.input(files=('inputs/day1.txt')):
    l.append(int(line))

for i, x in enumerate(l, start=0):
    looking = 2020 - x
    for y in l[i:]:
        if looking == y:
            print(looking * x);

for i, x in enumerate(l, start=0):
    looking = 2020 - x
    for j, y in enumerate(l[i:], start=i):
        looking2 = looking - y
        for z in l[j:]:
            if looking2 == z:
                print(looking2 * x * y);

