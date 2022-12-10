def is_reportable_time(t):
    return (t - 20) % 40 == 0 and t < 221


def process_instructions(instructions):
    instruction_stack = list(reversed(instructions))
    register = 1

    while instruction_stack:
        instruction = instruction_stack.pop()
        if instruction == "noop":
            yield register
        else:
            increment = int(instruction.split(" ")[1])
            yield register
            yield register

            register += increment


def register_and_cycles(instructions):
    for cycle_raw, reg in enumerate(process_instructions(instructions)):
        yield (cycle_raw + 1, reg)


def part_one(instructions):
    result = 0

    for cycle, register in register_and_cycles(instructions):
        if is_reportable_time(cycle):
            result += cycle * register

    print(result)


def crt_lines(instructions):
    current_row = []

    for cycle, r in register_and_cycles(instructions):
        current_row.append(r)

        if cycle % 40 == 0:
            yield current_row
            current_row = []


def calculate_pixel_value(pixel_render: int, sprite_val: int):
    if abs(pixel_render - sprite_val) > 1:
        return " "
    return "#"


def part_two(instructions):
    pixel_lines = map(
        lambda l: "".join(
            calculate_pixel_value(cycle, reg) for cycle, reg in enumerate(l)
        ),
        crt_lines(instructions),
    )

    for line in pixel_lines:
        print(line)


def main():
    with open("day10_input_orig", "r") as f:
        instructions = [l.strip() for l in f.readlines()]

    part_one(instructions)
    part_two(instructions)


main()