import fileinput, math, bisect
import functools
filename = "inputs/day7.txt"

def get_single_bag_contains(bag_desc):
    # Number, desc1 desc 2  bags
    l = bag_desc.strip().split()
    num = int(l[0])
    desc = l[1] + " " + l[2]
    return desc, num

# Desc to [(desc, num),...]
bags = {}

for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    if len(line_data) == 0:
        continue
    bag_rule = line.split("contain")
    holder = bag_rule[0].split(" bags")[0]
    containers = bag_rule[1].split(",")
    contains = []
    for container in containers:
        if container.strip().startswith("no"):
            continue
        contains.append(get_single_bag_contains(container))
    bags[holder] = contains

class BagNode:
    def __init__(self, description, contains):
        self.description = description
        self.contains = contains # List of bag nodes?



def count_bag_holders(looking, count):
    for bag_desc, contain_list in bags.items():
        for c in contain_list:
            if c[0] == looking:
                next = bag_desc
                if next not in count:
                    count.append(next)
                count_bag_holders(next, count)

def count_total_bags(looking):
    #print("Looking for " + looking)
    contain_list = bags[looking]
    this_count = 0
    for c in contain_list:
        desc = c[0]
        num = c[1]
        this_count += num  + (num * count_total_bags(desc))
    #print(this_count)
    return this_count

looking = "shiny gold"
count = []
#print(bags)
count_bag_holders(looking, count)
print("Part 1: " + str(len(count)))

print("Part 2: " + str(count_total_bags(looking)))