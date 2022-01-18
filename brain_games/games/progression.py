#!/usr/bin/env python3
from random import randrange

GAME_RULE = 'What number is missing in the progression?'

SEQ_LEN_BASE = 6
SEQ_LEN_TOP = 11
SEQ_TERM_BASE = 2
SEQ_TERM_TOP = 31
SEQ_DIFF_BASE = 2
SEQ_DIFF_TOP = 11


def make_sequence(
    seq_len: int,
    init_term: int,
    seq_diff: int
) -> list:
    return [init_term + seq_diff * i for i in range(seq_len)]


# takes index of term in the sequence, replaces it w/ '..'
def cut_term(sequence, term_index):
    num = sequence[term_index]
    sequence[term_index] = '..'
    return num


# returns two strings of sorts 'question', 'solution'
def get_game_strings():
    sequence = make_sequence(
        randrange(SEQ_LEN_BASE, SEQ_LEN_TOP),
        randrange(SEQ_TERM_BASE, SEQ_TERM_TOP),
        randrange(SEQ_DIFF_BASE, SEQ_DIFF_TOP))
    
    num = cut_term(sequence, randrange(len(sequence)))

    solution_line = str(num)

    sequence = [str(i) for i in sequence]
    sequence_line = ' '.join(sequence)
    return sequence_line, solution_line
