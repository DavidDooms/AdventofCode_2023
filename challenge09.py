"""Advent of Code: Day 9"""

import pandas as pd
import numpy as np

test_in = [[0, 3, 6, 9, 12, 15],
           [1, 3, 6, 10, 15, 21],
           [10, 13, 16, 21, 30, 45]]

with open('data/input09.txt') as f:
    lines = f.readlines()


def read_info(info: list):
    code = np.array(info)

    while np.sum(code[-1]) != 0:
        if np.ndim(code) == 1:
            new_row = np.append(np.diff(code), 0)
        else:
            new_row = np.append(np.diff(code[-1]), 0)
        nonzero_indices = np.nonzero(new_row)[0]
        if len(nonzero_indices) > 0:
            last_nonzero = new_row[nonzero_indices[-1]]
            i = 1
            while new_row[-i] == 0:
                new_row[-i] = last_nonzero
                i += 1
        code = np.vstack([code, new_row])
    return code


if __name__ == "__main__":
    check = [read_info(t) for t in lines]
    check_sum = [np.sum(c[:, -1]) for c in check]
    #print(check)
    #print(check_sum)
    print(sum(check_sum))
