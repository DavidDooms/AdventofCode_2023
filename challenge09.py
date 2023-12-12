"""Advent of Code: Day 9"""

import pandas as pd
import numpy as np

test_in = [[0, 3, 6, 9, 12, 15],
           [1, 3, 6, 10, 15, 21],
           [10, 13, 16, 21, 30, 45]]

with open('data/input09.txt') as f:
    lines = f.readlines()

data = []
for line in lines:
    line = line.replace('\n', '').split()
    line = [int(x) for x in line]
    data.append(line)


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


def fill_patern(info: list):
    pat_dic = {0: info}
    last_line = info
    counter = 1
    while last_line != [0 for j in range(len(last_line))]:
        new_line = []
        for i in range(len(last_line)-1):
            new_line.append(last_line[i+1] - last_line[i])
        last_line = new_line
        pat_dic[counter] = new_line
        counter += 1
    return pat_dic


def complete_patern(dic: dict):
    m = max(dic.keys())
    dic[m].append(0)
    for i in range(m-1, -1, -1):
        dic[i].append(dic[i+1][-1] + dic[i][-1])
    return dic


def complete_patern_front(dic: dict):
    m = max(dic.keys())
    dic[m].insert(0, 0)
    for i in range(m - 1, -1, -1):
        dic[i].insert(0, dic[i][0] - dic[i + 1][0])
    return dic


if __name__ == "__main__":
    #  check = [read_info(t) for t in lines]
    #  check_sum = [np.sum(c[:, -1]) for c in check]
    #  print(check)
    #  print(check_sum)
    #  print(sum(check_sum))

    """Part one
    check = [fill_patern(t) for t in data]
    print(check)
    test = [complete_patern(c) for c in check]
    print(test)
    result = [d[0][-1] for d in test]
    print(result)
    print(sum(result))"""

    """Part two"""
    check = [fill_patern(t) for t in data]
    print(check)
    test = [complete_patern_front(c) for c in check]
    print(test)
    result = [d[0][0] for d in test]
    print(result)
    print(sum(result))
