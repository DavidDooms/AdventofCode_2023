"""Advent of Code: day 13"""

from sympy import Matrix

with open('data/input13.txt') as f:
    lines = f.readlines()

test_code = ["#.##..##.",
             "..#.##.#.",
             "##......#",
             "##......#",
             "..#.##.#.",
             "..##..##.",
             "#.#.##.#.",
             "",
             "#...##..#",
             "#....#..#",
             "..##..###",
             "#####.##.",
             "#####.##.",
             "..##..###",
             "#....#..#"]


def adapt_input(list_in: list):
    list_out = []
    mat = Matrix()
    for line in list_in:
        if line.strip() == "":
            list_out.append(mat)
            mat = Matrix()
        else:
            line = line.replace("\n", "")
            line = [s for s in line]
            mat = mat.row_insert(mat.rows, Matrix([line]))
    return list_out


def v_check(mat: Matrix):
    pass


def h_check(mat: Matrix):
    pass


if __name__ == "__main__":
    print(test_code)
    matrices = adapt_input(test_code)
    print(matrices)
