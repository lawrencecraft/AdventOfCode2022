from dataclasses import dataclass
from typing import Callable
from time import time


@dataclass
class Monkey:
    monkey_id: int
    items: list[int]
    operation: Callable[[int], int]
    test_divisible: int
    true_monkey: int
    false_monkey: int


OP_2_OP = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x // y,
    '*': lambda x, y: x * y
}


def get_operand(token, arg):
    if token == 'old':
        return arg
    return int(token)


def parse_operation(operation: str):
    tokens = operation.split(' ')

    def execute_operation(i: int) -> int:
        left = tokens[0]
        right = tokens[2]

        op_function = OP_2_OP[tokens[1]]

        return op_function(get_operand(left, i), get_operand(right, i))

    return execute_operation


def parse_monkey(input_stack: list[str]):
    # starting line - get monkey id
    monkey_id = int(input_stack.pop().strip(':').split(' ')[1])

    # starting items
    starting_item_row = input_stack.pop()
    starting_items = [int(i) for i in starting_item_row.split(': ')[
        1].strip().split(', ')]

    # operation line
    operation_raw = input_stack.pop().split(' = ')[-1]
    operation = parse_operation(operation_raw)

    # divisibile line
    divisible_by = int(input_stack.pop().split(' ')[-1])

    # True line
    true_monkey = int(input_stack.pop().split(' ')[-1])
    # False line
    false_monkey = int(input_stack.pop().split(' ')[-1])

    monkey = Monkey(monkey_id=monkey_id,
                    items=starting_items,
                    operation=operation,
                    test_divisible=divisible_by,
                    true_monkey=true_monkey,
                    false_monkey=false_monkey)

    # Get rid of the newline
    if input_stack:
        input_stack.pop()

    return monkey


def parse_monkeys(lines) -> list[Monkey]:
    input_stack = list(reversed(lines))

    while input_stack:
        yield parse_monkey(input_stack)


def perform_round(monkeys: list[Monkey], worry_adjustment: int):
    monkey_scores = [0 for _ in monkeys]

    for idx, monkey in enumerate(monkeys):
        items = monkey.items
        monkey_scores[idx] += len(items)
        monkey.items = []

        new_item_scores = [worry_adjustment(i) for i in map(monkey.operation, items)]

        for item in new_item_scores:
            dest_monkey = monkey.true_monkey if item % monkey.test_divisible == 0 else monkey.false_monkey
            monkeys[dest_monkey].items.append(item)

    return monkey_scores


def execute_rounds(monkeys: list[Monkey], num_rounds: int, worry_adjustment: Callable[[int], int]):
    monkey_scores = [0 for _ in monkeys]

    for _ in range(num_rounds):
        new_scores = perform_round(monkeys, worry_adjustment)
        monkey_scores = list(map(sum, zip(monkey_scores, new_scores)))

    top_two = list(sorted(monkey_scores, reverse=True))[:2]
    print(top_two[0] * top_two[1])

def part_one(monkeys: list[Monkey]):
    return execute_rounds(monkeys, 20, lambda x: x // 3)

def part_two(monkeys: list[Monkey]):
    monkey_product = 1
    for monkey in monkeys:
        monkey_product *= monkey.test_divisible

    return execute_rounds(monkeys, 10000, lambda x: x % monkey_product)

def main():
    with open('day11_input', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    monkey_list_one = list(parse_monkeys(lines))
    monkey_list_two = list(parse_monkeys(lines))

    part_one(monkey_list_one)
    part_two(monkey_list_two)


if __name__ == "__main__":
    main()
