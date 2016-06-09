from Stacks.postfix_evaluation import postfix_evaluation

assert postfix_evaluation('5 2 ^ 3 *') == 75
assert postfix_evaluation('1 2 3 * + 5 -') == 2
assert postfix_evaluation('2 3 1 * + 9 -') == -4
assert postfix_evaluation('5 6 2 + * 12 4 / -') == 37