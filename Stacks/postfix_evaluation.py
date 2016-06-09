from Stacks.stack import Stack
from utility.utility import is_number
"""
1) List all binary operands
2) Split the expression by spaces.  Also create a function to figure out if a token is a number.
3) Go through the expression one by one from left to right.
4) If token is a number, push to stack.
5) If token is an operand, pop the top item, call it variable two.  Pop another and that will be variable one.
6) Now, apply the one operand two. (Math operation). Push result back to stack.
7) Continue till end.
8) Pop the result from stack and return.
"""


BINARY_OPERANDS = {'*', '/', '+', '-', '^'}

def postfix_evaluation(expression):
    results = Stack()
    tokens = expression.split(' ')

    for token in tokens:
        if is_number(token):
            results.push(int(token))
        else:
            if token in BINARY_OPERANDS and not results.is_empty():
                second = results.pop()
                first = results.pop()
                results.push(do_math(first, second, token))
    print(results.peek())
    return results.pop()

def do_math(operator, operator2, operand):
    if operand == '*':
       return operator * operator2
    elif operand == '/':
        return operator / operator2
    elif operand == '+':
        return operator + operator2
    elif operand == '-':
        return operator - operator2
    elif operand == '^':
        return operator ** operator2
