def calculate_row_visibility(row):
    max_seen_tree = None
    visibility_stats = [False for _ in row]

    for idx, val in enumerate(row):
        if max_seen_tree is None or max_seen_tree < val:
            visibility_stats[idx] = True
            max_seen_tree = val

    max_seen_tree = None
    for idx, val in reversed(list(enumerate(row))):
        if max_seen_tree is None or max_seen_tree < val:
            visibility_stats[idx] = True
            max_seen_tree = val

    return visibility_stats


def print_treedom(visibility):
    for row in visibility:
        print("".join("O" if t else " " for t in row))

    print(sum(1 if t else 0 for row in visibility for t in row), "visible trees")


def part_one(trees: list[list[int]]):
    tree_visibility = []

    # Do the rows
    for row in trees:
        visibility = calculate_row_visibility(row)
        tree_visibility.append(visibility)

    # Do the columns
    for col_idx in range(len(trees[0])):
        column = [row[col_idx] for row in trees]
        visibility = calculate_row_visibility(column)

        for row_idx, val in enumerate(visibility):
            tree_visibility[row_idx][col_idx] = tree_visibility[row_idx][col_idx] or val

    print_treedom(tree_visibility)


def bigger_trees(tree_row: list[int], size):
    for idx, tree in enumerate(tree_row):
        if tree >= size:
            return idx + 1

    return len(tree_row)


def calculate_scenic(trees: list[list[int]], row_idx, col_idx):
    if not row_idx or not col_idx or row_idx == len(trees) or col_idx == len(trees[0]):
        return 0

    tree_row = trees[row_idx]
    tree_column = [row[col_idx] for row in trees]

    trees_right = tree_row[col_idx + 1 :]
    trees_left = list(reversed(tree_row[:col_idx]))
    trees_up = tree_column[row_idx + 1 :]
    trees_down = list(reversed(tree_column[:row_idx]))

    return (
        bigger_trees(trees_right, trees[row_idx][col_idx])
        * bigger_trees(trees_left, trees[row_idx][col_idx])
        * bigger_trees(trees_down, trees[row_idx][col_idx])
        * bigger_trees(trees_up, trees[row_idx][col_idx])
    )


def all_scenic(trees: list[list[int]]):
    # pylint: disable=consider-using-enumerate
    for row_idx in range(len(trees)):
        for col_idx in range(len(trees[row_idx])):
            yield calculate_scenic(trees, row_idx, col_idx)


def part_two(trees: list[list[int]]):
    print(max(all_scenic(trees)))


def main():
    with open("day08_input_orig", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    trees = [[int(x) for x in l] for l in lines]
    part_one(trees)
    part_two(trees)


main()
