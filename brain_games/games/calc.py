#!/usr/b:win/env python3
from random import randrange

GAME_RULE = 'What is the result of the expression?'

OP_CHARS = ['+', '-', '*']

INT_BASE = 2
INT_TOP = 100
INT_MUL_BASE = 2
INT_MUL_TOP = 12


# returns two strings of sorts ('question', 'solution')
def get_game_strings():
    operator = OP_CHARS[randrange(len(OP_CHARS))]

    if operator == '+' or operator == '-':
        num_0 = randrange(INT_BASE, INT_TOP)
        num_1 = randrange(INT_BASE, INT_TOP)
    elif operator == '*':
        num_0 = randrange(INT_BASE, INT_TOP)
        num_1 = randrange(INT_MUL_BASE, INT_MUL_TOP)

    question_line = f"{num_0} {operator} {num_1}"
    solution_line = str(eval(question_line))

    return question_line, solution_line
