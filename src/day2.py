import numpy as np
import pandas as pd

example = """A Y
B X
C Z"""


def score(opponent, you):
    mat = np.matrix("3 6 0;0 3 6;6 0 3")
    df = pd.DataFrame(mat, index=["A", "B", "C"], columns=["X", "Y", "Z"])
    # print(res)

    shape = {"X": 1, "Y": 2, "Z": 3}

    return df.loc[opponent][you] + shape[you]


def part1(text):
    lines = text.splitlines()

    total_score = 0
    for line in lines:
        opp = line.split()[0]
        you = line.split()[1]
        total_score += score(opp, you)

    return total_score


def score_res(opponent, res):
    mat = np.matrix("3 4 8;1 5 9;2 6 7")
    df = pd.DataFrame(mat, index=["A", "B", "C"], columns=["X", "Y", "Z"])
    return df.loc[opponent][res]


def part2(text):
    lines = text.splitlines()

    total_score = 0
    for line in lines:
        opp = line.split()[0]
        res = line.split()[1]
        total_score += score_res(opp, res)

    return total_score


if __name__ == "__main__":
    text_input = open("data/day2.txt", "r").read()

    print("1. Example : ", part1(example))
    print("1. Input : ", part1(text_input))

    print("-" * 100)

    print("2. Example : ", part2(example))
    print("2. Input : ", part2(text_input))
