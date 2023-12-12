"""Advent of Code: Day 4"""

with open('data/input04.txt') as f:
    lines = f.readlines()

lines2 = []
for rows in lines:
    rows = rows.replace("\n", "")
    lines2.append(rows)

my_nums = []
winning_nums = []
for rows in lines2:
    my_nums.append(rows.split(":")[1].split("|")[0].split())
    winning_nums.append(rows.split("|")[1].split())

# This is for part one
points = [0 for i in range(len(my_nums))]
for i in range(len(my_nums)):
    for num in my_nums[i]:
        if num in winning_nums[i]:
            points[i] += 1

points_def = [2**(point - 1) for point in points if point != 0]

# This if for part two
cards = [1 for i in range(len(my_nums))]
cards_used = [1 for i in range(len(my_nums))]
for i in range(len(my_nums)):
    while cards_used[i] > 0:
        winners = 1
        for num in my_nums[i]:
            if num in winning_nums[i]:
                cards[i + winners] += 1
                cards_used[i + winners] += 1
                winners += 1
        cards_used[i] -= 1

    """winners = 1
    for num in my_nums[i]:
        if num in winning_nums[i]:
            cards[i + winners] += 1
            winners += 1"""

if __name__ == "__main__":
    print(my_nums)
    print(winning_nums)
    # All for part one
    print(points)
    # print(sum(points_def))

    """ All for part two"""
    print(cards)
    print(cards_used)
    print(sum(cards))

