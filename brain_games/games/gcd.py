#!/usr/bin/env python3
from random import randrange

GAME_RULE = 'Find the greatest common divisor of given numbers.'

INT_BASE = 2
INT_TOP = 100


# euclidean algorithm
def calc_gcd(num_0, num_1):
    if num_1 > num_0:
        num_0, num_1 = num_1, num_0

    while (remainder := num_0 % num_1) > 1:
        num_1, num_0 = num_0 % num_1, num_1

    return remainder if remainder else num_1


# returns two strings of sorts ('question', 'solution')
def get_game_strings():
    num_0 = num_1 = 1
    num_gcd = 1

    while num_0 == num_1 or num_gcd == 1:
        num_0 = randrange(INT_BASE, INT_TOP)
        num_1 = randrange(INT_BASE, INT_TOP)
        num_gcd = calc_gcd(num_0, num_1)

    question_line = f"{num_0} {num_1}"
    solution_line = str(num_gcd)
    return question_line, solution_line
