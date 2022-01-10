#!/usr/b:win/env python3

from brain_games.core import make_randint_array
from random import randint

MATH_OPCODES = ['nop', 'sum', 'sub', 'mul']
opcodes = []


# makes random int list [x, y, z] for op codes
def init_game(step_count):
    global opcodes
    opcodes = make_randint_array(step_count, 1, 3)


def compose_expression(num_0, num_1, op_text):
    op_char = '+' if op_text == 'sum' else '-' if op_text == 'sub' else '*'
    expression = f"{num_0} {op_char} {num_1}"
    return expression


# returns list ['question', 'solution']
def exec_game_step(step):
    def make_text_expression():
        nonlocal question_line
        nonlocal solution_line
        nonlocal num_0, num_1
        nonlocal operator

        question_line = compose_expression(num_0, num_1, operator)
        solution_line = str(eval(question_line))

    question_line = 'NoS'
    solution_line = 'NoS'
    operator = MATH_OPCODES[opcodes[step]]
    if operator == 'sum' or operator == 'sub':
        num_0 = randint(3, 99)
        num_1 = randint(3, 99)
    elif operator == 'mul':
        num_0 = randint(11, 99)
        num_1 = randint(3, 9)
    make_text_expression()
    return [question_line, solution_line]
