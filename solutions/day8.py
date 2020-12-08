import fileinput, math, bisect
import functools
filename = "inputs/day8.txt"
acc = 0


def execute(op, exec_index):
    # returns the next index to run
    o = op[0]
    v = op[1]
    #print("Executing " + str(op))
    if o == "jmp":
        return exec_index + v
    elif o == "acc":
        global acc
        acc += v
        return exec_index + 1
    return exec_index + 1


def get_operation(st):
    return st.split()[0], int(st.split()[-1])

ops = []
indices = []
for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    op, v = get_operation(line_data)
    ops.append((op, v))

def execute_operations(exec_index):
    while exec_index not in list(map(lambda x: x[0], indices)):
        if (exec_index >= len(ops)):
            return True
        indices.append((exec_index, acc))
        exec_index = execute(ops[exec_index], exec_index)
        #print(exec_index)
    # We've hit a loop
    #  TODO back track
    return False

execute_operations(0)
print("Part 1: " + str(acc))


def swap(i):
    #print("Swapping index: " + str(i))
    #print(ops[i])
    op = ops[i];
    if (op[0] == "nop"):
        ops[i] = ("jmp", op[1])
    elif op[0] == "jmp":
        ops[i] = ("nop", op[1])
    #print("To")
    #print(ops[i])

def pop_until_swappable():
    #print(indices)
    i = indices.pop();
    currOp = ops[i[0]]
    op = currOp[0]
    while(op != "nop" and op != "jmp"):
        i = indices.pop();
        currOp = ops[i[0]]
        op = currOp[0]
    return i
        

def perform_fix(exec_index):
    while len(indices) > 0:
        global acc
        currAcc = acc
        # We've hit a loop
        # pop the stack until a swappable element
        exec_index = pop_until_swappable()
        # swap
        swap(exec_index[0])
        acc = exec_index[1]
        #continue executing
        if (execute_operations(exec_index[0])):
            # success
            return
        else:
            # pop stack until back at index
            while True:
                if (exec_index == indices.pop()):
                    break;
            # reset acc
            acc = currAcc
            # swap back
            swap(exec_index[0])
            # continue popping

new_exec_index = indices.pop()
print("Performing fix starting at:" + str(new_exec_index))
perform_fix(new_exec_index[0])
print("Part 2: " + str(acc))

