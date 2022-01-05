#!/usr/b:win/env python3
from ..cli import welcome_user
from ..core import brain_games_exec, unique_rand_list
from random import seed, randint

GAME_STEPS_COUNT = 3
MATH_OP_LIST = ['nop', 'sum', 'sub', 'mul']


def task_init():
    op_list = []

    seed(None)
    op_list = unique_rand_list(GAME_STEPS_COUNT, 1, 3)
    return op_list


# takes randomly ordered list [x, y, z] for op codes
# returns list ['question', 'solution']
def task_calc(op_list, step):
    if MATH_OP_LIST[op_list[step]] == 'sum' or\
            MATH_OP_LIST[op_list[step]] == 'sub':
        num_0 = randint(3, 99)
        num_1 = randint(3, 99)
        if MATH_OP_LIST[op_list[step]] == 'sum':
            question_line = f'{num_0} + {num_1}'
            solution_line = str(num_0 + num_1)
        else:
            question_line = f'{num_0} - {num_1}'
            solution_line = str(num_0 - num_1)
    elif MATH_OP_LIST[op_list[step]] == 'mul':
        num_0 = randint(11, 99)
        num_1 = randint(3, 9)
        question_line = f'{num_0} * {num_1}'
        solution_line = str(num_0 * num_1)
    return [question_line, solution_line]


def input_validate(input_str):
    if input_str.lstrip('-').isdigit():
        return True
    return False


def answer_validate(input_str, solution_str):
    if input_str == solution_str:
        return True
    return False


def main():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    prompt_line = 'What is the result of the expression?'
    brain_games_exec(user_name, prompt_line, task_init, task_calc,
                     GAME_STEPS_COUNT, input_validate, answer_validate)


if __name__ == '__main__':
    main()
