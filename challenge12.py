"""Advent of Code: Day 12"""

import functools

with open('data/input12.txt') as f:
    lines = f.readlines()

test_correct = ["#.#.### 1,1,3",
                ".#...#....###. 1,1,3",
                ".#.###.#.###### 1,3,1,6",
                "####.#...#... 4,1,1",
                "#....######..#####. 1,6,5",
                ".###.##....# 3,2,1"]

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


def checker(patern: str, damaged: list):
    l_patern = patern.split(".")
    l_patern = [len(x) for x in l_patern]
    l_patern = [x for x in l_patern if x > 0]
    damages = [int(x) for x in damaged]
    if l_patern == damages:
        return 1
    return 0


def fill(patern: str, damaged: list):
    sum = 0
    if "?" not in patern:
        sum += checker(patern, damaged)
        return sum
    else:
        return fill(patern.replace("?", ".", 1), damaged) + fill(patern.replace("?", "#", 1), damaged)


if __name__ == "__main__":
    data = adapt_input(lines)
    print(data)

    check = [checker(d[0], d[1]) for d in data]
    print(check)

    test = [fill(d[0], d[1]) for d in data]
    print(test)
    print(sum(test))
