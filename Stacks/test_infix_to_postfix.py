from Stacks.infix_to_postfix import infix_to_postfix

assert infix_to_postfix('A * B + C') == 'A B * C +'
assert infix_to_postfix('A * (B + C)') == 'A B C + *'
assert infix_to_postfix('3 + 4 * 5 / 6') == '3 4 5 * 6 / +'
assert infix_to_postfix('A * B + C * D') == 'A B * C D * +'
assert infix_to_postfix('A + B + C + D') == 'A B + C + D +'
assert infix_to_postfix('(A + B) * (C + D)') == 'A B + C D + *'
assert infix_to_postfix('5^2 * 3') == '5 2 ^ 3 *'
assert infix_to_postfix('5 ^ 12 * 3') == '5 12 ^ 3 *'