#!/usr/bin/env python3

from brain_games.core import make_randint_array
from random import randint

game_list = []


# makes list of 3 lists [length, start_num, prog_step, skip_index]
def init_game(step_count):
    global game_list
    len_list = start_list = step_list = skip_list = []
    len_list = make_randint_array(step_count, 6, 10)
    start_list = make_randint_array(step_count, 2, 20)
    step_list = make_randint_array(step_count, 2, 5)
    for i in range(step_count):
        skip_list.append(randint(0, len_list[i] - 1))
    for i in range(step_count):
        game_list.append([len_list[i], start_list[i], step_list[i],
                         skip_list[i]])


# returns list ['question', 'solution']
def exec_game_step(step):
    prog_len = game_list[step][0]
    start_num = game_list[step][1]
    prog_step = game_list[step][2]
    skip_ndx = game_list[step][3]

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
