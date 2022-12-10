from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int


@dataclass
class Node:
    name: str
    dirs: list["Node"]
    files: list[File]
    parent: "Node"
    total_size: int


def build_filesystem():
    with open("day07_input_orig", "r") as f:
        lines: list[str] = [l.strip() for l in f.readlines()]
        # current_dir = []
        root_node = None
        current_node: Node = None

        while lines:
            line = lines[0]

            if line.startswith("$ cd "):
                dir = line[len("$ cd ") :]
                print(dir)

                if dir == "..":
                    current_node = current_node.parent
                else:
                    new_node = Node(
                        name=dir, dirs=[], files=[], parent=current_node, total_size=0
                    )

                    if current_node:
                        current_node.dirs.append(new_node)

                    current_node = new_node

                    if not root_node:
                        root_node = current_node

                lines = lines[1:]

            elif line.startswith("$ ls"):
                lines = lines[1:]

                while lines and not lines[0].startswith("$"):
                    line = lines[0]

                    if not line.startswith("dir"):
                        size, name = line.split(" ")
                        file = File(name, int(size))

                        current_node.files.append(file)

                    lines = lines[1:]

        return root_node


def print_fs(node: Node, depth=0):
    print(f"{'  ' * depth}- {node.name} (dir, total_size={node.total_size})")

    for child in node.dirs:
        print_fs(child, depth + 1)

    for file in node.files:
        print(f"{'  ' * depth}  - {file.name} (file, size={file.size})")


def get_total_size_and_mark(node: Node):
    file_in_dir = sum(file.size for file in node.files)
    sub_dirs = sum(get_total_size_and_mark(child) for child in node.dirs)

    total_size = file_in_dir + sub_dirs
    node.total_size = total_size

    return total_size


def part_one(root: Node):
    nodes = [root]
    total = 0

    while nodes:
        node = nodes.pop()
        if node.total_size <= 100000:
            total += node.total_size

        for child in node.dirs:
            nodes.append(child)

    print(total)


def part_two(root: Node):
    smallest_node = root
    nodes = [root]

    space_available = 70000000 - root.total_size
    space_required = 30000000 - space_available

    while nodes:
        node = nodes.pop()
        if node.total_size < smallest_node.total_size and node.total_size >= space_required:
            smallest_node = node

        for child in node.dirs:
            nodes.append(child)

    print(smallest_node.total_size)


def main():
    filesystem = build_filesystem()
    get_total_size_and_mark(filesystem)
    print_fs(filesystem)

    part_one(filesystem)
    part_two(filesystem)


main()