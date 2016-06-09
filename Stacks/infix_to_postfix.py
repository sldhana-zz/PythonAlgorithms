from Stacks.stack import Stack
from utility.utility import is_number

PRECEDENCE = {
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}
BRACKETS = ['(', ')']
APPROVED_APLPHABETS = 'ABCDEFGHIJKLMNOPQESTUVWXYZ'

def infix_to_postfix(expression):
    operator_stack = Stack()
    converted = []
    expression = expression.split(' ')
    alphabets = list(APPROVED_APLPHABETS)

    for character in expression:
        # check if the character is a number or an alphabet, if so, add directly to the converted string
        if character in alphabets or is_number(character):
            converted.append(character)
        else:
            # if character is an operand, use the precedence dictionary to figure weight
            if character in PRECEDENCE:
                if not operator_stack.is_empty():
                    # we need to check if the character on top of stack is '('.  If so, just add the current character.
                    if operator_stack.peek() == '(':
                        operator_stack.push(character)
                    # If it's not a '(', then check the precedence. Only add if current character precedence is lower.
                    # Else, pop off the current item, add it to the converted string, and then push the current character.
                    elif PRECEDENCE[operator_stack.peek()] >= PRECEDENCE[character]:
                        converted.append(operator_stack.pop())
                        operator_stack.push(character)
                    # If smaller precedence, just add to operator stack.
                    else:
                        operator_stack.push(character)
                else:
                    # if empty, we just push character to stack
                    operator_stack.push(character)
            # check if character is either '(' or ')'/  If opening bracket, add to stack.
            elif character in BRACKETS:
                if character == '(':
                    operator_stack.push(character)
                # if it's closing bracket, we need to find the matching ')'.  So pop it until we find the '(' on top.
                else:
                    # pop the stack until find the matching '('
                    while not operator_stack.is_empty():
                        if operator_stack.peek() != '(':
                            converted.append(operator_stack.pop())
                        else:

                            operator_stack.pop()


    # no more character, pop stack and add to converted
    while not operator_stack.is_empty():
        converted.append(operator_stack.pop())

    return ' '.join(converted)

