#!/usr/bin/env python3
from random import randrange

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

INT_TOP = 100


def is_prime(num):
    if num < 2:
        return False

    divisor = 2

    while divisor <= num / 2:
        if num % divisor == 0:
            return False
        divisor += 1
    return True


# returns two strings of sorts ('question', 'solution')
def get_game_strings():
    number = randrange(INT_TOP)

    solution_line = 'yes' if is_prime(number) else 'no'
    question_line = str(number)
    return question_line, solution_line
