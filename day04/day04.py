import string


def encompasses(i1, i2):
    return i1[0] <= i2[0] and i1[1] >= i2[1]


def does_overlap(i1, i2):
    intervals = [i1, i2] if i1[0] < i2[0] else [i2, i1]

    lowest, highest = intervals

    return lowest[1] >= highest[0]


def main():
    with open("day04_input", "r") as f:
        lines = (l.strip().split(",") for l in f.readlines())
        ranges = [map(lambda x: [int(p) for p in x.split("-")], line) for line in lines]
        encomp = 0
        overlap = 0

        for interval1, interval2 in ranges:
            fully_encompasses = encompasses(interval1, interval2) or encompasses(
                interval2, interval1
            )

            overlaps = does_overlap(interval1, interval2)

            if fully_encompasses:
                encomp += 1

            if overlaps:
                overlap += 1

        # Part 1
        print(encomp)

        # Part 2
        print(overlap)


main()
