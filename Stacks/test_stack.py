from Stacks.stack import Stack

s = Stack()
s.push(1)
s.push(2)
assert s.is_empty() == False
assert s.peek() == 2

s.pop()
assert s.peek() == 1
s.pop()
assert s.is_empty() == True
assert s.pop() == None
