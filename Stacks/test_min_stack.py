from Stacks.min_stack import MinStack


min_stack = MinStack()
min_stack.push(10)
min_stack.push(20)
assert min_stack.min() == 10
min_stack.push(-1)
assert min_stack.min() == -1
min_stack.push(20)
min_stack.push(50)
min_stack.push(30)
assert min_stack.min() == -1
min_stack.pop()
min_stack.pop()
min_stack.pop()
min_stack.pop()
assert min_stack.min() == 10