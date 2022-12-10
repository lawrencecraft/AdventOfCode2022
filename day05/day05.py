import string

from dataclasses import dataclass


@dataclass
class Move:
    source: int
    destination: int
    quantity: int


uppercase_set = set(string.ascii_uppercase)


def extract_container_definition_lines(lines):
    for line in lines:
        if line == "":
            break

        yield line


def extract_moves(lines: list[str]):
    for line in lines:
        if line.startswith("move"):
            yield line


def parse_stack_line(line: str, stacks: list[list]):
    current_stack = 0
    line_stack = list(
        reversed(line)
    )  #  We will treat the line as a stack here, so get it into stack form

    while line_stack:
        head_token = line_stack.pop()
        if head_token == "[":
            # This is a container def
            container_id = line_stack.pop()

            # Strip the end token as well and space if it exists
            line_stack.pop()

            stacks[current_stack].append(container_id)
        elif head_token == " ":
            # We've hit a space row. Pop the three
            line_stack.pop()
            line_stack.pop()
        else:
            raise Exception(f"Bad row - {line_stack}")

        if line_stack:
            line_stack.pop()

        current_stack += 1


def build_container_definitions(lines):
    stacks = []
    definition_lines = reversed(
        list(extract_container_definition_lines(lines)))

    first_line = next(definition_lines)

    # Just assume single digit
    for char in first_line:
        if char in string.digits:
            stacks.append([])

    # Parse out the stacks
    for line in definition_lines:
        parse_stack_line(line, stacks)

    return stacks


def parse_move(line):
    tokens = line.split(" ")
    return Move(
        quantity=int(tokens[1]),
        source=int(tokens[3]) - 1,
        destination=int(tokens[5]) - 1,
    )


def part_one(lines):
    stacks = build_container_definitions(lines)

    # Execute moves
    moves = (parse_move(m) for m in extract_moves(lines))

    for move in moves:
        for _ in range(move.quantity):
            crate = stacks[move.source].pop()
            stacks[move.destination].append(crate)

    print("".join(stack[-1] for stack in stacks))


def part_two(lines):
    stacks = build_container_definitions(lines)

    # Execute moves
    moves = (parse_move(m) for m in extract_moves(lines))

    for move in moves:
        to_add = []
        for _ in range(move.quantity):
            crate = stacks[move.source].pop()
            to_add.append(crate)

        while to_add:
            stacks[move.destination].append(to_add.pop())

    print("".join(stack[-1] for stack in stacks))


def main():
    with open("day05_input", "r") as f:
        lines = [l.strip("\n") for l in f.readlines()]

        part_one(lines)
        part_two(lines)


main()
