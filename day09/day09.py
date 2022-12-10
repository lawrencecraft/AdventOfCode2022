def calculate_tail_move(head_position: tuple[int, int], tail_position: tuple[int, int]):
    x_difference = head_position[0] - tail_position[0]
    y_difference = head_position[1] - tail_position[1]

    # If they're next to each other, we're okay
    if abs(x_difference) <= 1 and abs(y_difference) <= 1:
        return tail_position

    # Dumb hack. We can offset by just sign modified to 1
    x_offset = x_difference // abs(x_difference) if x_difference else 0
    y_offset = y_difference // abs(y_difference) if y_difference else 0

    return (tail_position[0] + x_offset, tail_position[1] + y_offset)


DIRECTION_OFFSET_MAP = {"R": (1, 0), "U": (0, 1), "D": (0, -1), "L": (-1, 0)}


def tail_position_calculation(chain_length: int, moves: list[tuple[str, int]]):
    chain = [(0, 0)] * chain_length

    tail_positions = set()
    tail_positions.add((0, 0))

    # Iterate through moves
    for direction, distance in moves:
        offset = DIRECTION_OFFSET_MAP[direction]

        for _ in range(distance):
            # Move the head, stretch the chain
            head = chain[0]
            new_head_position = (head[0] + offset[0], head[1] + offset[1])
            new_chain = [new_head_position]
            last_link = new_head_position

            for link in chain[1:]:
                new_link_position = calculate_tail_move(last_link, link)
                new_chain.append(new_link_position)
                last_link = new_link_position

            chain = new_chain

            tail_positions.add(chain[-1])
    return len(tail_positions)


def part_one(moves: list[tuple[str, int]]):
    print(tail_position_calculation(2, moves))


def part_two(moves: list[tuple[str, int]]):
    print(tail_position_calculation(10, moves))


def main():
    moves: list[tuple[str, int]]
    with open("day09_input_orig", "r") as f:
        moves_raw = [l.strip().split(" ") for l in f.readlines()]
        moves = [(d, int(v)) for d, v in moves_raw]

    part_one(moves)
    part_two(moves)


main()