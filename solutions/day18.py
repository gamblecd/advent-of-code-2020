import fileinput, bisect, operator
import functools
filename = "inputs/day18_Ex.txt"


class OperatorNode:
    def __init__(self, oper, t1, t2):
        self.oper = oper
        self.t1 = t1
        self.t2 = t2

    def eval(self):
        #print("eval:", self.oper, self.t1.eval(), self.t2.eval())
        return self.oper(self.t1.eval(), self.t2.eval())

class NumberNode:
    def __init__(self, t1):
        self.t1 = t1

    def eval(self):
        return int(self.t1)    

def parse(tokens, root):
    curr = tokens
    while not len(curr) == 0:
        op = curr[0]
        t1 = curr[1]
        if op == "+":
            op = operator.add
            if (root.oper == operator.mul):
                node = OperatorNode(op, NumberNode(t1), root.t2)
                root.t2 = node
            else:
                root = OperatorNode(op, root, NumberNode(t1))
        if op == "*":
            op = operator.mul
            if (root.oper == operator.add):
                root = OperatorNode(op, root, NumberNode(t1))
            else:
                root = OperatorNode(op, root, NumberNode(t1))
        curr = curr[2:]
    return root
def calculate(tokens):
    if len(tokens) == 1:
        return NumberNode(tokens[0])
    # elif len(tokens) == 3:
    #     #Part 1
    #     t1 = tokens[0]
    #     t2 = tokens[1]
    #     t3 = tokens[2]

    #     op = None
    #     if t2 == "+":
    #         op = operator.add
    #     if t2 == "*":
    #         op = operator.mul
    #     z = op(int(t1), int(t3))
    #     return calculate([z] + tokens[3:])
    else:
        tokens.reverse()
        t1 = tokens[0]
        t1 = NumberNode(t1)
        t2 = tokens[1]
        t3 = tokens[2]
        if t2 == "+":
            op = operator.add
        if t2 == "*":
            op = operator.mul

        root = OperatorNode(op, t1,NumberNode(t3))

        root = parse(tokens[3:], root)
        return root.eval()
        print()

stack = [[]]
def math(rest):
    if len(rest) == 0:
        return
    t = rest[0]
    if t == "(":
        stack.append([])
    elif t == ")":
        n = calculate(stack.pop())
        stack[-1].append(n)
    else:
        curr = stack[-1]
        curr.append(t)
    math(rest[1:])
s = 0
for line in fileinput.input(files=(filename)):
    line_data = line.strip()
    line_data = line_data.replace("(", " ( ").replace(")", " ) ")
    tokens = line_data.split()
    stack = [[]]
    math(tokens)
    n = calculate(stack[-1])
    print(n)
    s += n
print("Part 1: ", s)
print()
print("Part 2: ",)
