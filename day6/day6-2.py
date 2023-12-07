from day6 import solver


def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        time, distance = [], []
        time.append(int(lines[0].strip().split(":")[1].replace(" ", "")))
        distance.append(int(lines[1].strip().split(":")[1].replace(" ", "")))
    return zip(time, distance)


def main():
    return solver(read_input())


if __name__ == '__main__':
    print(main())
