def find_uniq(signal, window_size):

    for idx in range(window_size, len(signal) + 1):
        window = signal[idx - window_size : idx]

        if len(set(window)) == window_size:
            print(idx)
            return


def main():
    with open("day06_input", "r") as f:
        signal = f.readline().strip()

        find_uniq(signal, 4)
        find_uniq(signal, 14)


main()