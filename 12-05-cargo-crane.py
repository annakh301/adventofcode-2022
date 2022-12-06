import read_function
import re

moves = read_function.read_file("input-puzzle/rearrangement-instructions.csv")

print(moves)

def remove_words(text):
    rep = {"move ": "", "from ": "stack", "to " : "stack"} # define desired replacements here
    # use these three lines to do the replacement
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    #Python 3 renamed dict.iteritems to dict.items so use rep.items() for latest versions
    pattern = re.compile("|".join(rep.keys()))
    input_numbers = pattern.sub(lambda m: rep[re.escape(m.group(0))], text).split(" ")
    return input_numbers


def mover9000(times, from_stack, to_stack):
    counter = 0
    stack_list_from = globals()[from_stack]
    stack_list_to = globals()[to_stack]
    while counter<times:
        popped = stack_list_from.pop()
        stack_list_to.append(popped)
        counter = counter + 1

def mover9001(times, from_stack, to_stack):
    counter = 0
    stack_list_from = globals()[from_stack]
    stack_list_to = globals()[to_stack] 
    temp = [] 
    while counter<times:
        popped = stack_list_from.pop()
        temp.append(popped)
        counter = counter + 1
    stack_list_to.extend(temp[::-1])

stack1 = ['D', 'B', 'J', 'V']
stack2 = ['P', 'V', 'B', 'W', 'R', 'D', 'F']
stack3 = ['R', 'G', 'F', 'L', 'D', 'C', 'W', 'Q']
stack4 = ['W', 'J', 'P', 'M', 'L', 'N', 'D', 'B']
stack5 = ['H', 'N', 'B', 'P', 'C', 'S', 'Q']
stack6 = ['R', 'D', 'B', 'S', 'N', 'G']
stack7 = ['Z', 'B', 'P', 'M', 'Q', 'F', 'S', 'H']
stack8 = ['W', 'L', 'F']
stack9 = ['S', 'V', 'F', 'M', 'R']

for movement in moves:
    times, from_stack, to_stack = remove_words(movement)
    mover9001(int(times), from_stack, to_stack)

print(stack1)
print(stack2)
print(stack3)
print(stack4)
print(stack5)
print(stack6)
print(stack7)
print(stack8)
print(stack9)

result = stack1[-1:]  + stack2[-1:] + stack3[-1:] + stack4[-1:] + stack5[-1:] + stack6[-1:] + stack7[-1:] + stack8[-1:] + stack9[-1:]
print(result)
# traverse in the string
str = ""
for ele in result:
    str += ele
print(str)