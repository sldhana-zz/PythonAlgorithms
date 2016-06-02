from Stacks.balanced_expresssion import is_balanced_expression

assert is_balanced_expression('(a + b)')
assert not is_balanced_expression('2.3 + 23 / 12 + ( 3.14 * .24')
assert is_balanced_expression('2.3 + 23 / 12 + ( 3.14 * .24 )')
assert is_balanced_expression('{{([][])}()}')
assert not is_balanced_expression('{{([][{])}()}')
assert not is_balanced_expression('{)(a,b}')