"""Advent of Code: Day 6"""

races = [(46, 208), (85, 1412), (75, 1257), (82, 1410)]  # Time, Distance
racetwo = [(46857582, 208141212571410)]
races_test = [(7, 9), (15, 40), (30, 200)]  # Time, Distance
racetwo_test = [(71530, 940200)]


# make a function to test how far we can go
def get_distances(time: int):
    dists = [(time, 0)]
    for i in range(time):
        dists.append((i, (time-i)*i))
    return dists


# make a function to see the first above record time
def get_nr_distances(time: int, record: int, first=True):
    if first:
        i = 0
        while ((time-i)*i) < record:
            i += 1
    else:
        i = time
        while ((time - i) * i) < record:
            i -= 1
    return i


# make a function to count how many are above record
def count_records(attempts: list, record):
    passed = 0
    for i in range(len(attempts)):
        if attempts[i][1] > record:
            passed += 1
    return passed


def multiply_list(my_list):
    # Multiply elements one by one
    result = 1
    for x in my_list:
        result = result * x
    return result


if __name__ == "__main__":
    """ First part, MemoryError for second part
    tests = [(get_distances(r[0]), r[1]) for r in racetwo]
    print(tests)
    check = [count_records(t[0], t[1]) for t in tests]
    print(check)
    print(multiply_list(check))
    """

    what = get_nr_distances(racetwo_test[0][0], racetwo_test[0][1])
    why = get_nr_distances(racetwo_test[0][0], racetwo_test[0][1], first=False)
    print(what)
    print(why)

    whatwhat = get_nr_distances(racetwo[0][0], racetwo[0][1])
    whywhy = get_nr_distances(racetwo[0][0], racetwo[0][1], first=False)
    print(what)
    print(why)
    print(whywhy-whatwhat+1)
