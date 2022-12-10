import string


def part_one():
    with open("day03_input", "r") as f:
        lines = (l.strip() for l in f.readlines())
        total_sum = 0

        for backpack in lines:
            first_container = set(backpack[: len(backpack) // 2])
            second_container = set(backpack[len(backpack) // 2 :])

            matched = first_container.intersection(second_container).pop()
            score = string.ascii_letters.index(matched) + 1

            total_sum += score

        print(total_sum)


def part_two():
    with open("day03_input", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        total_sum = 0

        for i in range(0, len(lines), 3):
            first, second, third = [set(x) for x in lines[i : i + 3]]
            group_common = first.intersection(second).intersection(third).pop()

            score = string.ascii_letters.index(group_common) + 1
            total_sum += score
        print(total_sum)


def main():
    part_one()
    part_two()


main()
