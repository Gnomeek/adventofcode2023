from day4 import read_input


def solver(winnings, picks):
    cnt = 0
    for i in picks:
        if i in winnings:
            cnt += 1
    print(winnings, picks, cnt)
    return 2**(cnt-1) if cnt != 0 else 0


def main():
    res = sum([solver(*i) for i in read_input()])
    print(res)


if __name__ == '__main__':
    main()
