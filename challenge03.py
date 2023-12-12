"""Advent of Code: Day 3"""

import pandas as pd

with open('data/input03.txt') as f:
    lines = f.readlines()

matrix = []

symbol = ['/', '&', '%', '$', '@', '#', '=', '*', '-', '+']

for rows in lines:
    rows = rows.replace("\n", "")
    matrix.append([e for e in rows])

df_in = pd.DataFrame(matrix)


def add_numbers(df: pd.DataFrame):
    numbers = []
    nr, nc = df.shape
    num = ''
    has_symbol = False
    for i in range(nr):
        for j in range(nc):
            if df.loc[i, j].isnumeric():
                num = num + df.loc[i, j]
                if check_around(df, i, j, symbol):
                    has_symbol = True
            else:
                if has_symbol:
                    numbers.append(num)
                num = ''
                has_symbol = False
    return numbers


def check_around(df: pd.DataFrame, row: int, col: int, symbols):
    """check if a certain location in a DataFrame has a list of symbols around it"""
    pairs_to_check = [(row, col + 1), (row, col - 1), (row + 1, col + 1), (row + 1, col), (row + 1, col - 1),
                      (row - 1, col + 1), (row - 1, col), (row - 1, col - 1)]
    if row == 0:
        pairs_to_check.remove((row - 1, col + 1))
        pairs_to_check.remove((row - 1, col))
        pairs_to_check.remove((row - 1, col - 1))
    if col == 0:
        try:
            pairs_to_check.remove((row - 1, col - 1))
        except ValueError:
            pass
        pairs_to_check.remove((row, col - 1))
        pairs_to_check.remove((row + 1, col - 1))
    if row == df.shape[0] - 1:
        pairs_to_check.remove((row + 1, col + 1))
        pairs_to_check.remove((row + 1, col))
        pairs_to_check.remove((row + 1, col - 1))
    if col == df.shape[1] - 1:
        pairs_to_check.remove((row - 1, col + 1))
        pairs_to_check.remove((row, col + 1))
        try:
            pairs_to_check.remove((row + 1, col + 1))
        except ValueError:
            pass

    for r, c in pairs_to_check:
        if df.loc[r, c] in symbols:
            return True

    return False


if __name__ == "__main__":
    nrow, ncol = df_in.shape
    # print(nrow)
    # print(ncol)
    lijst = add_numbers(df_in)
    print(lijst)
    print(sum([int(e) for e in lijst]))

    """FUCK YOU MIJN TEST WERKT, MAAR HET GROTE NIET!!!!"""

    #print(df_in.loc[0, 7])
    #check = check_around(df_in, 0, 7, symbol)
    #print(check)
