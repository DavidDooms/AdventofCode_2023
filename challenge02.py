"""Advent of Code: Day 2"""

limit = {'red': 12, 'green': 13, 'blue': 14}

def input_to_dict(input: list):
    result = {}
    for line in input:
        gameno = line.split(":")[0]
        gamesets = line.split(":")[1]
        result[gameno] = gamesets.split(";")
    return result

def str_to_dict(s: str):
    gamedict = {'red': 0, 'green': 0, 'blue': 0}
    s = s.split(",")
    temp = []
    for i in s:
        temp.extend(i.split())
    for color in gamedict:
        for i in range(len(temp)):
            if temp[i] == color:
                gamedict[color] = int(temp[i-1])
    return gamedict

with open('data/input02.txt') as f:
    lines = f.readlines()

if __name__ == "__main__":
    # First part
    d = input_to_dict(lines)
    d2 = {}
    for k, v in d.items():
        temp_list = []
        for i in v:
            temp_list.append(str_to_dict(i))
        d2[k] = temp_list
    """
    impossibles = []
    for k in d2:
        for grab in d2[k]:
            if (grab['red'] > limit['red']) or (grab['blue'] > limit['blue']) or (grab['green'] > limit['green']):
                impossibles.append(int(k.split()[1]))
    possibles = [i for i in range(101) if i not in impossibles]

    print(impossibles)
    print(possibles)
    print(sum(possibles))"""

    # Second part
    min_dict = {}
    for k in d2:
        min_game = {'red': 0, 'green': 0, 'blue': 0}
        for grab in d2[k]:
            if grab['red'] > min_game['red']:
                min_game['red'] = grab['red']
            if grab['green'] > min_game['green']:
                min_game['green'] = grab['green']
            if grab['blue'] > min_game['blue']:
                min_game['blue'] = grab['blue']
        min_dict[k] = min_game

    power_dict = {}
    for k in min_dict:
        power_dict[k] = min_dict[k]['red']*min_dict[k]['green']*min_dict[k]['blue']
    print(power_dict)

    power_list = [v for v in power_dict.values()]

    print(sum(power_list))
