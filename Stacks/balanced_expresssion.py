from Stacks.stack import Stack

"""
Time complexity: 0(n) because we're scanning each character.
Space complexity: 0(n) because it depends on the number of characters in the stack.
"""


def is_balanced_expression(expression):
    """
    Put the closing symbols as the key, and the opening as the value as we want
    to match on closing.
    """
    SYMBOLS = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    symbols = Stack()

    for i in expression:
        # add if it's opening symbol into stack
        if i in SYMBOLS.values():
            symbols.push(i)
        # if closing symbol, check against the stack if we can find its opening pair.
        elif i in SYMBOLS.keys():
            # we need to check if the popped value matches the closing pair
            if not symbols.is_empty():
                popped = symbols.pop()
                if popped != SYMBOLS[i]:
                    return False
            # if the stack is empty with closing, this is an immediate short circuit for an invalid expression.
            else:
                return False

    return symbols.is_empty()




