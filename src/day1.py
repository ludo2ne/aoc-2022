example = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def calories_dict(text):
    lines = text.splitlines()

    calories = 0
    dict_elves = dict()
    elve_num = 1

    for food in lines:
        if not food:
            dict_elves[elve_num] = calories
            elve_num += 1
            calories = 0
        else:
            calories += int(food)

    dict_elves[elve_num] = calories

    return dict_elves


def part1(text):
    dict_elves = calories_dict(text)
    return max(dict_elves.values())


def part2(text):
    dict_elves = calories_dict(text)
    calories_by_elve = list(dict_elves.values())
    calories_by_elve.sort(reverse=True)
    return sum(calories_by_elve[:3])


if __name__ == "__main__":
    text_input = open("data/day1.txt", "r").read()

    print("1. Example : ", part1(example))
    print("1. Input : ", part1(text_input))

    print("-" * 100)

    print("2. Example : ", part2(example))
    print("2. Input : ", part2(text_input))
