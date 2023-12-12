"""Advent of Code: Day 12"""

with open('data/input09.txt') as f:
    lines = f.readlines()

test_code = ["???.### 1,1,3",
             ".??..??...?##. 1,1,3",
             "?#?#?#?#?#?#?#? 1,3,1,6",
             "????.#...#... 4,1,1",
             "????.######..#####. 1,6,5",
             "?###???????? 3,2,1"]


def adapt_input(list_in: list):
    list_out = []
    for line in list_in:
        list_out.append((line.split()[0], [int(x) for x in line.split()[1].split(",")]))
    return list_out


if __name__ == "__main__":
    data = adapt_input(test_code)
    print(data)
