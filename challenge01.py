"""Advent of Code: Day 1"""

def get_first_and_last(s: str):
    numbers = [str(i) for i in range(10)]
    i = 0
    while s[i] not in numbers:
        i=i+1
    first = s[i]
    i = 1
    while s[-i] not in numbers:
        i=i+1
    last = s[-i]
    return int(first+last)

def change_number(s: str):
    digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
              'nine': '9'}
    #for d in digits:
    #    s = s.replace(d, digits[d])
    indices = {word: -1 for word in digits}

    for word in digits:
        if word in s:
            index = s.find(word, indices[word] + 1)
            indices[word] = index
    indices = replace_negative_values(indices)
    word = min(indices, key = indices.get)
    s = s[:indices[word]] + digits[word] + s[indices[word] + len(word):]

    return s

def replace_negative_values(d):
    for key, value in d.items():
        if value < 0:
            d[key] = 999
    return d

def change_all_numbers(s: str):
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for word in digits:
        while word in s:
            s = change_number(s)
    return s

with open('data/input01.txt') as f:
    lines = f.readlines()

test = ['two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen']

if __name__ == "__main__":
    # First part
    # numlines = [get_first_and_last(s) for s in lines]
    # print(sum(numlines))

    # Second part
    updatedlines1 = [change_all_numbers(s) for s in lines]
    numlines1 = [get_first_and_last(s) for s in updatedlines1]
    print(sum(numlines1))
    #Ik neem gevallen niet mee zoals "eightwo", eigenlijk moet ik de twee nog vinden, maar ik vind enkel de acht.
    
    # stolencode
    updatedlines = [s.replace("one", "o1e").replace("two", "t2o").replace("three", "th3tee").replace("four", "f4r")
                    .replace("five", "f5e").replace("six", "s6x").replace("seven", "se7en").replace("eight", "ei8ht")
                    .replace("nine", "n9ne") for s in lines]
    numlines = [get_first_and_last(s) for s in updatedlines]
    print(sum(numlines))

    for i in range(len(updatedlines)):
        if numlines1[i] != numlines[i]:
            print(updatedlines1[i])
            print(updatedlines[i])
