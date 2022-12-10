SCORES = "XYZ"
OPP = "ABC"
OPP_WINS = {"A": "Z", "B": "X", "C": "Y"}


def hand_score(hand):
    return SCORES.index(hand) + 1


def winner_points(opp, you):
    their_pos = OPP.index(opp)
    your_pos = SCORES.index(you)

    if their_pos == your_pos:
        return 3

    return 0 if you == OPP_WINS[opp] else 6


def part_2_hand(opp, you):
    offset = SCORES.index(you) - 1
    their_pos = OPP.index(opp)

    return SCORES[(offset + their_pos) % 3]


def main():
    with open("day02_input", "r") as f:
        lines = (l.strip().split(" ") for l in f.readlines())
        total = 0
        part_2_total = 0

        for opp, you in lines:
            score = hand_score(you) + winner_points(opp, you)
            part_2 = part_2_hand(opp, you)

            total += score
            part_2_total += hand_score(part_2) + winner_points(opp, part_2)

            print(f"{opp} {you} - {part_2}: {score}")

        print(f"total: {total}")
        print(f"part2 total: {part_2_total}")


main()
