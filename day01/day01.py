def main():
    elves = []
    with open("day01_p1_input", "r") as f:
        current_elf = 0
        lines = (l.strip() for l in f.readlines())

        for line in lines:
            if not line:
                if current_elf:
                    elves.append(current_elf)
                    current_elf = 0
            else:
                current_elf += int(line)

        if current_elf:
            elves.append(current_elf)
    
    # part 1
    print(max(elves))

    # part 2
    sorted_elves = sorted(elves, reverse=True)
    print(sum(sorted_elves[:3]))



main()
