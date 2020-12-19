import fileinput, bisect
import functools
filename = "inputs/day19.txt"

def eval(rules, term, starting_index, current_rules):
    # if (starting_index == len(term)):
    #     # we've gone too far
    #     return -1
    current_rule = current_rules[-1]
    curr = rules[current_rule]
    if type(curr) is str:
        try:
            if (curr == term[starting_index]):
                return starting_index
            else:
                return -1
        except:
            if (current_rules.count(8)) > 1:
                return starting_index
            return -1
            pass
    else:
        if (current_rule == '0'):
            # Recurse on 42
            # Then recurse on 42 and 31 and even amount of times
            indices = []
            index = starting_index
            rule_s = current_rules[:]
            depth = 0
            while(index < len(term)) and not (index == -1):
                rule_s.append("42")
                depth +=1
                index = eval(rules, term, index, rule_s)
                if (index == -1):
                    if (depth == 1):
                        return -1
                    #no match, do something
                    pass
                else:
                    indices.append(index)
                    index += 1
                    # Keep track of viable options
            # Now we have to find any cases where handling 11 works for index
            viable = []
            indices_31 = []
            for i, ind in enumerate(indices):
                index = ind + 1
                depth = 0
                while(index < len(term)) and not (index == -1):
                    rule_s.append("31")
                    depth +=1
                    index = eval(rules, term, index, rule_s)
                    if (index == -1):
                        #no match, do something
                        # ignore
                        pass
                    else:
                        indices_31.append(index)
                        index += 1
                        # Keep track of viable options
            #To succeed, there needs to be at least one usage of 31
            if len(indices_31) >= len(indices):
                return -1
            if len(indices_31) > 0:
                return indices_31[-1] 
            # elif len(indices)>0 and (indices[-1]) == len(term):
            #      return indices[-1]
            else:
                return -1
        # Assume list
        if type(curr[0]) == list:
            # if current_rule == '8':
            #     recurse_level = 1
            #     index = starting_index-1
            #     last_success = starting_index-1
            #     while index < len(term) or index == -1:
            #         index = starting_index-1
            #         rule_s = current_rules[:]
            #         for i in range(recurse_level):
            #             rule_s.append('42')
            #             # eval 42 i times
            #             index = eval(rules, term, index+1, rule_s)
            #             if (index == -1):
            #                 return -1
            #         if not (index == -1):
            #             last_success = index
            #         index +=1
            #         recurse_level +=1
            #     return index - 1
            # if current_rule == '11':
            #     # Case 1 is the firt version of case 2
            #     # try until we are out of range
            #     recurse_level = 1
            #     index = starting_index-1
            #     last_success = starting_index-1
            #     while index < len(term) or index == -1:
            #         index = starting_index-1
            #         rule_s = current_rules[:]
            #         for i in range(recurse_level):
            #             rule_s.append('42')
            #             # eval 42 i times
            #             index = eval(rules, term, index+1, rule_s)
            #             if (index == -1):
            #                 return -1
            #         for i in range(recurse_level):
            #             rule_s.append('31')
            #             # eval 31 the same amount of times
            #             index = eval(rules, term, index+1, rule_s)
            #             if (index == -1):
            #                 # ignore this failure, 
            #                 # could be 
            #                 break
            #         if not (index == -1):
            #             last_success = index
            #         index +=1
            #         recurse_level +=1
            #     return index - 1

            # Or case
            for l in curr:
                index = starting_index
                rule_set = current_rules[:]
                for r in l:
                    rule_set.append(r)
                    index = eval(rules, term, index, rule_set)
                    if (index == -1):
                        # Did not match
                        break
                    else:
                        index += 1 # matched, continue checking for the next index
                if not index == -1:
                    # If one matched, we can continue
                    # Is that accurate? do we need both for sure?
                    return index-1
            # If we get here, no matches found
            return -1
        else:
            is_valid = True
            index = starting_index
            rule_set = current_rules[:]
            for r in curr:
                rule_set.append(r)
                index = eval(rules, term, index, rule_set)
                if (index == -1):
                    # Did not match
                    return index
                else:
                    index += 1 # matched, continue checking for the next index
            return index-1

with open(filename) as fp: 
    rules = {}
    new_rules = {}
    line_data = fp.readline().strip()
    while not len(line_data) == 0:
        # Define Rules
        name_and_value = line_data.split(":")
        rule_name = name_and_value[0]
        if "|" in name_and_value[1]:
            # Or set
            rule_list = name_and_value[1].strip().split("|")
            rule_or_list = []
            for rule in rule_list:
                # List of rule names
                r = rule.split()
                rule_or_list.append(r)
            rules[rule_name] = rule_or_list
        elif '"' in name_and_value[1]:
            rules[rule_name] = name_and_value[1].strip()[1] # Single char
        else: 
            rule_list = name_and_value[1].strip().split()
            rules[rule_name] = rule_list
        new_rules[rule_name] = name_and_value[1].strip()
        line_data = fp.readline().strip()
    print(rules)

    # mappers = {}
    # for k, v in new_rules.items():
    #     if v.startswith('"'):
    #         new_rules[k] = v[1]
    #         mappers[k] = v[1]
    # modifications = True
    # while modifications:
    #     additions = {}
    #     for k, v in new_rules.items():
    #         curr_string = v
    #         for m, mv in mappers.items():
    #             spl = curr_string.split()
    #             if m in spl:
    #                 curr_string = " ".join([ mv if x == m else x for x in spl])
    #                 new_rules[k] =curr_string
            
    #         if not any(char.isdigit() for char in curr_string):
    #             if k not in mappers.keys(): 
    #                 if "|" in curr_string:
    #                     curr_string = "( " + curr_string +  " )"
    #                 additions[k] = curr_string
    #     if additions:
    #         mappers.update(additions)
    #         modifications = True
    #     else:
    #         modifications = False
    # # print(mappers)
    # # for k,v in new_rules.items():
    # #     print(k, v)


    line_data = fp.readline().strip()
    s = 0
    while not len(line_data) == 0:
        t = line_data
        index = eval(rules, t, 0, ["0"]) 
        if (len(t) - index != 1) and not (index == -1):
            print()
            print(len(t), index)
            print()
        else:
            print(len(t), index)

        if len(t) == index + 1:
            s += 1
            #print("pass")
            #print("fail")
        line_data = fp.readline().strip()
    print("Part 1: ", s)
print()
print("Part 2: ",)
