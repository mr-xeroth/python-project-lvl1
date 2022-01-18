#!/usr/bin/env python3
from random import randrange

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'

INT_TOP = 100


def is_odd(num):
    return num % 2 != 0


# returns two strings of sorts ('question', 'solution')
def get_game_strings():
    rand_num = randrange(INT_TOP)

    solution_line = 'no' if is_odd(rand_num) else 'yes'
    question_line = str(rand_num)
    return question_line, solution_line
