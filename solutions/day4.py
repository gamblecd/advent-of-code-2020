import fileinput, re
filename = "inputs/day4.txt"

valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]



def in_range(t, bottom, top):
    #print("Checking range for " + t + " -> " + str(bottom) + "-" + str(top))
    t = int(t)
    if bottom <= t and t <= top:
        #print("PASS")
        return True
    else:
        #print("FAIL")
        return False

def is_height(x):
    #print("Checking Height: " + x);
    metric = x[-2:]
    num = x[:-2]
    #print(metric, num)
    if metric == "in":
        return in_range(num, 59, 76)
    if metric == "cm":
        return in_range(num, 150, 193)

    return False

def is_passport(x):
    #print("Checking passport Id for " + t)
    return len(x) == 9 and x.isnumeric()

def is_color(x):
    m = re.match(r"^#[0-9A-Fa-f]{6}$", x)
    return m is not None



valid_entries = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #ignore cid
def validate(passportDict):
    #print("Size: " + str(len(passportDict)))
    for e in valid_entries:
        #print(e + ":" + str(e not in passportDict))
        if e not in passportDict:
            return False
    return True

validators = {"byr": lambda x: in_range(x, 1920, 2002),
              "iyr": lambda x: in_range(x, 2010, 2020),
              "eyr": lambda x: in_range(x, 2020, 2030),
              "hgt": lambda x: is_height(x),
              "hcl": lambda x: is_color(x),
              "ecl": lambda x: x in valid_eye_colors,
              "pid": lambda x: is_passport(x)}
def validation(passportDict):
    for k, v in validators.items():
        if k not in passportDict:
            #print("Missing " + k)
            return False
        else:
            if not v(passportDict[k]):
                #print("Invalid " + k + ": " + passportDict[k])
                return False
    return True

valid_count = 0
tough_valid_count = 0
passports = []
curr = {}


def run_validation(curr):
    #print(curr);
    passports.append(curr)
    if (validate(curr)):
        global valid_count
        valid_count += 1
    if validation(curr):
        global tough_valid_count
        tough_valid_count += 1


for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    if (len(line_data) == 0):
        run_validation(curr)
        curr = {}
    else:
        tokens = line_data.split()
        for t in tokens:
            entry = t.split(":")
            curr[entry[0]] = entry[1]

# Last line is not a empty line, so do the validation one more time. 
if (len(curr) > 0):
    run_validation(curr)
    curr = {}
print(len(passports))
print("Part 1: " + str(valid_count))
print("Part 2: " + str(tough_valid_count))