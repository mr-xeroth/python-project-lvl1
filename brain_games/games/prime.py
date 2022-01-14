#!/usr/bin/env python3

from random import randrange

PRIME_LIMIT = 100


def is_prime(num):
    if num < 2:
        return False

    divisor = 2

    while divisor <= num / 2:
        if num % divisor == 0:
            return False
        divisor += 1
    return True


# returns list ['question', 'solution']
def exec_game_step():
    number = randrange(PRIME_LIMIT)

    solution_line = 'yes' if is_prime(number) else 'no'
    question_line = str(number)
    return [question_line, solution_line]


exec_game_step.game_prompt = 'Answer "yes" if given number is prime. '\
                             'Otherwise answer "no".'
