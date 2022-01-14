#!/usr/b:win/env python3
from random import randint, sample

OP_CHARS = ['+', '-', '*']
op_char_cache = []


# returns list ['question', 'solution']
def exec_game_step():
    global op_char_cache

    if not op_char_cache:
        op_char_cache = sample(OP_CHARS, len(OP_CHARS))

    operator = op_char_cache[-1]
    op_char_cache.pop()

    if operator == '+' or operator == '-':
        num_0 = randint(3, 99)
        num_1 = randint(3, 99)
    elif operator == '*':
        num_0 = randint(11, 99)
        num_1 = randint(3, 9)

    question_line = f"{num_0} {operator} {num_1}"
    solution_line = str(eval(question_line))

    return [question_line, solution_line]


exec_game_step.game_prompt = 'What is the result of the expression?'
