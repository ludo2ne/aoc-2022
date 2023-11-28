import os
import re

example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def part1(text):
    lines = text.splitlines()
    res = 0

    for line in lines:
        e1, e2 = line.split(",")[0], line.split(",")[1]
        a, b = int(e1.split("-")[0]), int(e1.split("-")[1])
        c, d = int(e2.split("-")[0]), int(e2.split("-")[1])

        if (a <= c and b >= d) or (a >= c and b <= d):
            res += 1

    return res


def part2(text):
    lines = text.splitlines()
    res = len(lines)

    for line in lines:
        a, b, c, d = map(int, re.findall(r"\d+", line))

        if b < c or a > d:
            res -= 1

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
