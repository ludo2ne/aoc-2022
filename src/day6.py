import os

example = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""


def trouver_code(texte, taille) -> int:
    for i in range(taille, len(texte) + 1):
        if len(set(texte[i - taille : i])) == taille:
            return i


def part1(text):
    return trouver_code(text, 4)


def part2(text):
    return trouver_code(text, 14)


if __name__ == "__main__":
    day_num = "".join([n for n in os.path.basename(__file__) if n.isdigit()])
    input_path = "data/day" + day_num + ".txt"
    text_input = open(input_path, "r").read()

    print("1. Example : ", part1(example))
    print("1. Input : ", part1(text_input))

    print("-" * 100)

    print("2. Example : ", part2(example))
    print("2. Input : ", part2(text_input))
