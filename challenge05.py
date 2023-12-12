"""Advent of Code: Day 5"""

import pandas as pd

seed = [3127166940, 109160474, 3265086325, 86449584, 1581539098, 205205726, 3646327835, 184743451,
        2671979893, 17148151, 305618297, 40401857, 2462071712, 203075200, 358806266, 131147346,
        1802185716, 538526744, 635790399, 705979250]
seed_test = [79, 14, 55, 13]

column_names = ["destination", "source", "range"]
seed2soil = pd.read_csv('data/input05a.txt', sep=" ", skiprows=1, names=column_names)
soil2fert = pd.read_csv('data/input05b.txt', sep=" ", skiprows=1, names=column_names)
fert2water = pd.read_csv('data/input05c.txt', sep=" ", skiprows=1, names=column_names)
water2light = pd.read_csv('data/input05d.txt', sep=" ", skiprows=1, names=column_names)
light2temp = pd.read_csv('data/input05e.txt', sep=" ", skiprows=1, names=column_names)
temp2humid = pd.read_csv('data/input05f.txt', sep=" ", skiprows=1, names=column_names)
humid2loc = pd.read_csv('data/input05g.txt', sep=" ", skiprows=1, names=column_names)

seed2soil.sort_values(by="source", inplace=True, ignore_index=True)
soil2fert.sort_values(by="source", inplace=True, ignore_index=True)
fert2water.sort_values(by="source", inplace=True, ignore_index=True)
water2light.sort_values(by="source", inplace=True, ignore_index=True)
light2temp.sort_values(by="source", inplace=True, ignore_index=True)
temp2humid.sort_values(by="source", inplace=True, ignore_index=True)
humid2loc.sort_values(by="source", inplace=True, ignore_index=True)


def find_mapping(df: pd.DataFrame, value: int):
    if df.loc[0, "source"] > value:
        return value
    elif df.iloc[-1, 1] <= value:
        if df.iloc[-1, 1] + df.iloc[-1, 2] < value:
            return value
        else:
            dest = df.iloc[-1, 0]
            src = df.iloc[-1, 1]
            dif = value - src
            return dest + dif
    else:
        m_under = df["source"] <= value
        m_upper = df["source"].shift(-1) > value
        src = df.loc[m_under & m_upper, "source"].item()
        dest = df.loc[m_under & m_upper, "destination"].item()
        rge = df.loc[m_under & m_upper, "range"].item()
        if value < src + rge:
            dif = value - src
            return dest + dif
        else:
            return value


def creat_seed_list(list_in: list):
    list_out = []
    starts = list_in[::2]
    ranges = list_in[1::2]
    for i in range(len(starts)):
        list_out.extend([ele for ele in range(starts[i], starts[i] + ranges[i])])
    return list_out


def sequence(seedlist: list):
    # print(seedlist)
    soils = [find_mapping(seed2soil, i) for i in seedlist]
    # print(soils)
    ferts = [find_mapping(soil2fert, i) for i in soils]
    # print(ferts)
    waters = [find_mapping(fert2water, i) for i in ferts]
    # print(waters)
    lights = [find_mapping(water2light, i) for i in waters]
    # print(lights)
    temps = [find_mapping(light2temp, i) for i in lights]
    # print(temps)
    humids = [find_mapping(temp2humid, i) for i in temps]
    # print(humids)
    locs = [find_mapping(humid2loc, i) for i in humids]
    # print(locs)
    return locs


if __name__ == "__main__":
    #seeds = creat_seed_list(seed_test)

    starters = seed[::2]
    ranges = seed[1::2]

    minseed = -1

    for i in range(len(starters)):
        for ele in range(starters[i], starters[i] + ranges[i]):
    # for zaadje in seeds:
            locations = sequence([ele])
            if minseed == -1:
                minseed = locations[0]
            elif locations[0] < minseed:
                minseed = locations[0]
    print(minseed)
