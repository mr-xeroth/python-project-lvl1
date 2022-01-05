#!/usr/b:win/env python3
from ..cli import welcome_user
from ..core import brain_games_exec, unique_rand_list
from random import seed, randint

GAME_STEPS_COUNT = 3


def task_init():
    seed(None)
    len_list = start_list = step_list = skip_list = []
    len_list = unique_rand_list(GAME_STEPS_COUNT, 6, 10)
    start_list = unique_rand_list(GAME_STEPS_COUNT, 2, 20)
    step_list = unique_rand_list(GAME_STEPS_COUNT, 2, 5)
    for i in range(GAME_STEPS_COUNT):
        skip_list.append(randint(0, len_list[i] - 1))
    task_list = []
    for i in range(GAME_STEPS_COUNT):
        task_list.append([len_list[i], start_list[i], step_list[i],
                          skip_list[i]])
    return task_list


# takes list of 3 lists [length, start_num, prog_step, skip_index]
# returns list ['question', 'solution']
def task_progression(op_list, step):
    prog_len = op_list[step][0]
    start_num = op_list[step][1]
    prog_step = op_list[step][2]
    skip_ndx = op_list[step][3]

    prog_list = []
    next_num = start_num
    for i in range(prog_len):
        if i != skip_ndx:
            prog_list.append(str(next_num))
        else:
            solution_line = str(next_num)
            prog_list.append('..')
        next_num += prog_step
    prog_line = ' '.join(prog_list)
    return [prog_line, solution_line]


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
    prompt_line = 'What number is missing in the progression?'
    brain_games_exec(user_name, prompt_line, task_init, task_progression,
                     GAME_STEPS_COUNT, input_validate, answer_validate)


if __name__ == '__main__':
    main()
