import os
from string import ascii_letters

example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def part1(text):
    lines = text.splitlines()

    res = 0
    for line in lines:
        middle = len(line) // 2
        str_left, str_right = line[:middle], line[middle:]

        common_letter = list(set(str_left) & set(str_right))[0]
        p = ascii_letters.index(common_letter) + 1
        res += p

    return res


def part2(text):
    lines = text.splitlines()

    res = 0

    while lines:
        common_letter = list(set(lines[0]) & set(lines[1]) & set(lines[2]))[0]
        lines = lines[3:]
        res += ascii_letters.index(common_letter) + 1

    return res


if __name__ == "__main__":
    day_num = "".join([n for n in os.path.basename(__file__) if n.isdigit()])
    input_path = "data/day" + day_num + ".txt"
    text_input = open(input_path, "r").read()

    print("1. Example : ", part1(example))
    print("1. Input : ", part1(text_input))

    print("-" * 100)

    print("2. Example : ", part2(example))
    print("2. Input : ", part2(text_input))
