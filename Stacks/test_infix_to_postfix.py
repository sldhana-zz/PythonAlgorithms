from Stacks.infix_to_postfix import infix_to_postfix

assert infix_to_postfix('A * B + C') == 'AB*C+'
assert infix_to_postfix('A * (B + C)') == 'ABC+*'
assert infix_to_postfix('3+4 * 5/6') == '345*6/+'
assert infix_to_postfix('A * B + C * D') == 'AB*CD*+'
assert infix_to_postfix('A + B + C + D') == 'AB+C+D+'
assert infix_to_postfix('(A + B) * (C + D)') == 'AB+CD+*'
assert infix_to_postfix('5^2 * 3') == '52^3*'