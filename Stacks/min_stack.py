from Stacks.stack import Stack

# The time complexity to get the min in this stack is O(1)
# The space complexity is still O(n)

class MinStack():
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, item):
        self.stack.push(item)

        # if empty stack or item to be added is less
        # than the min_stack top item,
        # just push item into min stack
        if self.min_stack.is_empty() or \
            item < self.min_stack.peek():
            self.min_stack.push(item)
        # if not, add the top item in the min_stack to maintain min
        else:
            self.min_stack.push(self.min_stack.peek())

    def pop(self):
        popped = self.stack.pop()
        self.min_stack.pop()

        return popped

    def min(self):
        return self.min_stack.peek()

