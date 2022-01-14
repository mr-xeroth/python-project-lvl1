#!/usr/bin/env python3

from random import randrange

INT_LIMIT = 100


# euclidean algorithm
def calc_gdc(num_0, num_1):
    if num_1 > num_0:
        num_0, num_1 = num_1, num_0

    while (reminder := num_0 % num_1) > 1:
        num_1, num_0 = num_0 % num_1, num_1

    return reminder if reminder else num_1


# returns list ['question', 'solution']
def exec_game_step():
    num_0 = num_1 = 1
    num_gdc = 1

    while num_0 == num_1 or num_gdc == 1:
        num_0 = randrange(2, INT_LIMIT)
        num_1 = randrange(2, INT_LIMIT)
        num_gdc = calc_gdc(num_0, num_1)

    question_line = f"{num_0} {num_1}"
    solution_line = str(num_gdc)
    return [question_line, solution_line]


exec_game_step.game_prompt = 'Find the greatest '\
                             'common divisor of given numbers.'
