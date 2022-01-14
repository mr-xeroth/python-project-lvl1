#!/usr/bin/env python3

from random import randrange


def make_sequence():
    seq_len = randrange(6, 11)
    seq_init_term = randrange(2, 31)
    seq_diff = randrange(2, 10)
    return [seq_init_term + seq_diff * i for i in range(seq_len)]


# takes index of term, replaces it w/ '..'
def cut_term(sequence, term):
    num = sequence[term]
    sequence[term] = '..'
    return(num)


# returns list ['question', 'solution']
def exec_game_step():
    sequence = make_sequence()
    num = cut_term(sequence, randrange(len(sequence)))

    solution_line = str(num)

    sequence = [str(i) for i in sequence]
    sequence_line = ' '.join(sequence)
    return [sequence_line, solution_line]


exec_game_step.game_prompt = 'What number is missing in the progression?'
