import fileinput, math, bisect
import functools
filename = "inputs/day6.txt"

def ord97(cha):
    return ord(cha) - 97

def anyone(group):
    return functools.reduce(lambda v,e: v + 1 if e > 0 else v, group, 0)
    
def everyone(group, group_size):
    #print(group, group_size)
    return functools.reduce(lambda v,e: v + 1 if e == group_size else v, group, 0)

group = [ 0 for x in range(26)]

any_group_counts = []
all_group_counts = []
group_size = 0

for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    if len(line_data) == 0:
        # end group
        any_group_counts.append(anyone(group))
        all_group_counts.append(everyone(group, group_size))
        group = [ 0 for x in range(26)]
        group_size = 0
        continue

    group_size +=1

    for char in line_data:
        group[ord97(char)] += 1


any_group_counts.append(anyone(group))
all_group_counts.append(everyone(group, group_size))
group = [ 0 for x in range(26)]
group_size = 0

print(any_group_counts)
print(all_group_counts)
anytotal = functools.reduce(lambda v,e: v + e, any_group_counts, 0)
alltotal = functools.reduce(lambda v,e: v + e, all_group_counts, 0)
print(anytotal)
print(alltotal)