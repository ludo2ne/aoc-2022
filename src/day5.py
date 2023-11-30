import os
import re

example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


class Stack:
    def __init__(self, value):
        self.value = int(value)
        self.crates = []

    def add(self, val):
        self.crates.append(val)

    def move(self, number_crates, another_stack):
        while number_crates > 0:
            another_stack.crates.append(self.crates.pop())
            number_crates -= 1

    def move_bis(self, number_crates, another_stack):
        another_stack.crates.extend(self.crates[-number_crates:])
        del self.crates[-number_crates:]

    def __str__(self):
        return f"{self.value} : {[str(c) for c in self.crates]}"


def print_dict_stacks(stacks):
    print("*" * 30)
    for key, val in stacks.items():
        print(f"{key}: {val}")
    print("*" * 30)


def build_stacks(text):
    lines = text.splitlines()

    stack_num = 0

    while lines[stack_num]:
        stack_num += 1

    stack_num -= 1

    cols = lines[stack_num]

    stacks = dict()
    new_stacks = dict()

    for index, value in enumerate(cols):
        if value.isdigit():
            stacks[index] = Stack(value)

    for line in reversed(lines[:stack_num]):
        for index, value in enumerate(line):
            if value.isalpha():
                stacks[index].add(value)

    for s in stacks.values():
        new_stacks[s.value] = s

    return new_stacks


def moves_list(text, stacks):
    lines = text.splitlines()

    empty_row = 0

    while lines[empty_row]:
        empty_row += 1

    for line in lines[empty_row + 1 :]:
        m, f, t = map(int, re.findall(r"\d+", line))
        stacks[f].move(m, stacks[t])

    return stacks


def moves_list_bis(text, stacks):
    lines = text.splitlines()

    empty_row = 0

    while lines[empty_row]:
        empty_row += 1

    for line in lines[empty_row + 1 :]:
        m, f, t = map(int, re.findall(r"\d+", line))
        stacks[f].move_bis(m, stacks[t])

    return stacks


def part1(text):
    stacks = build_stacks(text)
    # print_dict_stacks(stacks)
    moves_list(text, stacks)
    # print_dict_stacks(stacks)

    res = ""
    for s in stacks.values():
        res += s.crates[-1]

    return res


def part2(text):
    stacks = build_stacks(text)
    # print_dict_stacks(stacks)
    moves_list_bis(text, stacks)
    # print_dict_stacks(stacks)

    res = ""
    for s in stacks.values():
        res += s.crates[-1]

    return res


if __name__ == "__main__":
    day_num = "".join([n for n in os.path.basename(__file__) if n.isdigit()])
    input_path = "data/day" + day_num + ".txt"
    text_input = open(input_path, "r").read()

    print("-" * 100)

    print("1. Example : ", part1(example))
    print("1. Input : ", part1(text_input))

    print("-" * 100)

    print("2. Example : ", part2(example))
    print("2. Input : ", part2(text_input))
