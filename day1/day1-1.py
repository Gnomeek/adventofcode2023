digits = [str(i) for i in range(10)]


def solver(line: str) -> int:
    tmp = ""
    for i in line:
        if i in digits:
            tmp += i
            break
    for i in line[::-1]:
        if i in digits:
            tmp += i
            break

    return int(tmp)


def main():
    res = 0
    with open("input.txt") as f:
        for l in f:
            res += solver(l)
    print(res)


if __name__ == '__main__':
    main()
