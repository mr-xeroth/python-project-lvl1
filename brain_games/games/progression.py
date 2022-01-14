#!/usr/bin/env python3

from random import randrange


# returns list ['question', 'solution']
def exec_game_step():
    seq_len = randrange(6, 11)
    seq_init_term = randrange(2, 31)
    seq_diff = randrange(2, 10)
    seq_skip = randrange(seq_len)

    seq_list = []
    next_term = seq_init_term

    for i in range(seq_len):
        if i != seq_skip:
            seq_list.append(str(next_term))
        else:
            solution_line = str(next_term)
            seq_list.append('..')
        next_term += seq_diff
    sequence_line = ' '.join(seq_list)
    return [sequence_line, solution_line]


exec_game_step.game_prompt = 'What number is missing in the progression?'
