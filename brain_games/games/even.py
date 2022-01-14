#!/usr/bin/env python3
from random import randrange

NUM_LIMIT = 100


def is_odd(num):
    return True if num % 2 else False


# returns list ['question', 'solution']
def exec_game_step():
    rand_num = randrange(NUM_LIMIT)

    solution_line = 'no' if is_odd(rand_num) else 'yes'
    question_line = str(rand_num)
    return [question_line, solution_line]


exec_game_step.game_prompt = 'Answer "yes" if the number is even, '\
                             'otherwise answer "no".'
