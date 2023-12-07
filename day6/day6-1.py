from day6 import solver


def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        time, distance = [], []
        for i in lines[0].strip().split(":")[1].split(" "):
            if i:
                time.append(int(i))
        for i in lines[1].strip().split(":")[1].split(" "):
            if i:
                distance.append(int(i))
    return zip(time, distance)


def main():
    return solver(read_input())


if __name__ == '__main__':
    print(main())
