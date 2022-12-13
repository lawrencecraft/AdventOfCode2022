import json
import functools


def compare_packet(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0

        return -1 if left < right else 1
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            result = compare_packet(l, r)

            if result != 0:
                return result

        if len(left) == len(right):
            return 0

        return compare_packet(len(left), len(right))
    elif isinstance(left, int) and isinstance(right, list):
        return compare_packet([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare_packet(left, [right])

    raise Exception(f"Unknown case: {left} {right}")


def part_one(lines):
    current_packet_idx = 0
    sum_packets = 0

    for idx in range(0, len(lines), 2):
        current_packet_idx += 1
        left = lines[idx]
        right = lines[idx + 1]

        if compare_packet(left, right) == -1:
            sum_packets += current_packet_idx

    print(sum_packets)


def part_two(lines):
    sorted_lines = list(
        sorted(lines, key=functools.cmp_to_key(compare_packet)))
    print((sorted_lines.index([[2]]) + 1) * (sorted_lines.index([[6]]) + 1))


def main():
    with open("day13_input", 'r') as f:
        lines = [json.loads(l.strip()) for l in f.readlines() if l != '\n']

    part_one(lines)
    part_two([*lines, [[2]], [[6]]])


if __name__ == "__main__":
    main()
