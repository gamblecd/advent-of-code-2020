import fileinput


def validate(num_range, letter, password):
    count = 0;
    for l in password:
        if l == letter:
            count = count + 1;
    if count >= num_range[0] and count <= num_range[1]:
        return 1
    else:
        return 0;

def validatePart2(position, letter, password):
    first = password[position[0]-1] == letter;
    second = password[position[1]-1] == letter;
    if (first or second) and not (first and second):
        return 1
    else:
        return 0;

l = [];
tc = 0;
tc2 = 0;
for line in fileinput.input(files=('inputs/day2.txt')):
    tokens = line.split()
    # range, letter, password
    # count letter, validate in range.
    num_range = list(map(lambda x: int(x), tokens[0].split("-")))
    letter = tokens[1].split(":")[0];
    password = tokens[2]
    tc = tc + validate(num_range, letter, password)
    tc2 = tc2 + validatePart2(num_range, letter, password)

print(tc)
print(tc2)
