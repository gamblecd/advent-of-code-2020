import fileinput, bisect
import functools
filename = "inputs/day16.txt"

invalid_values = []
rule_names = []
rule_satisfication = [] # List of dicts
rules = []
my_ticket_values = []
tickets = []
def check_ticket(ticket, rules):
    for i, x in enumerate(ticket):
        n = int(x)
        ok = False
        for j, r in enumerate(rules):
            for s in r:
                bottom= s[0]
                top = s[1]
                #print("Checking", n, "in", bottom, "-", top)
                if (n >= bottom and n <=top): #Satisfies at least 1

                    ok = True
                    break
            if ok:
                break
        if not ok:
            invalid_values.append(n)
            return False
    return True

def find_rules(ticket, rules):
    for i, x in enumerate(ticket):
        n = int(x)
        ok = False
        for j, r in enumerate(rules):
            for s in r:
                bottom= s[0]
                top = s[1]
                #print("Checking", n, "in", bottom, "-", top)
                if (n >= bottom and n <=top): #Satisfies at least 1
                    # Indicate the column and rule this was successful for
                    sat_dict = rule_satisfication[j]
                    sat_dict[i] = sat_dict.get(i, 0) + 1


with open(filename) as fp: 

    line_data = fp.readline().strip()
    while not len(line_data) == 0:
        tokens = line_data.split(": ")
        rule_name = tokens[0] # remove the 

        rule_values = tokens[1].split(" or ")
        rule_set = []
        for r in rule_values:
            rg = r.split("-")
            rule_set.append((int(rg[0]), int(rg[1])))
        rule_names.append(rule_name)
        rules.append(rule_set) # use a dict if we need the names
        line_data = fp.readline().strip()
    
    rule_satisfication = [{} for x in range(len(rules))]
    # Assume next line is "your ticket"
    line_data = fp.readline()
    my_ticket_values = list(map(int, fp.readline().strip().split(",")))
    #check_ticket(my_ticket_values, rules)
    # Assume next line is blank 
    line_data = fp.readline()
    # Then nearby tickets
    line_data = fp.readline()
    

    # First ticket
    line_data = fp.readline()
    while line_data:
        ticket = list(map(int, line_data.strip().split(",")))
        if (check_ticket(ticket, rules)):
            tickets.append(ticket)
        line_data = fp.readline()

p1 = sum(invalid_values)
print("Part 1: ", p1)

for t in tickets:
    find_rules(t, rules)

total_valid = len(tickets)
rule_valids = {}
for ri, rule in enumerate(rule_satisfication):
    for column, value in rule.items():
        if value == total_valid:
            # Rule works for column
            rule_name = rule_names[ri]
            rvl = rule_valids.get(rule_name, [])
            rvl.append(column)
            rule_valids[rule_name] = rvl
#print(rule_satisfication)
checkers = []

for ri, rule in rule_valids.items():
    #print(ri, rule)
    # if the length of rule is only 1, that MUST be the column it supports
    if len(rule) == 1:
        checkers.append((ri, rule[0]))

while not len(checkers) == 0:
    cn, cc = checkers[0]
    for ri2, rule2 in rule_valids.items():
        if not ri2 == cn:
            try:
                rule2.remove(cc)
                if len(rule2) == 1:
                    checkers.append((ri2, rule2[0]))
            except:
                pass
    checkers = checkers[1:]
# Given the Valid Tickets, which rule satisfies all values per column
#print()
s = 1
for ri, rule in rule_valids.items():
    #print(ri, rule)
    if ri.startswith("departure"):
        c = rule[0]
        s *= my_ticket_values[c]


print()
print("Part 2: ",s)
