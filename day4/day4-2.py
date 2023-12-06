from day4 import read_input


def solver(winnings, picks):
    cnt = 0
    for i in picks:
        if i in winnings:
            cnt += 1
    return cnt

def main():
    lines = read_input()
    card_dict = {i: 1 for i, _ in enumerate(lines, start=1)}
    for card_nr in card_dict.keys():
        hits = solver(*lines[card_nr-1])
        for j in range(hits):
            card_dict[card_nr+j+1] += card_dict[card_nr]

    print(sum(card_dict.values()))


if __name__ == '__main__':
    main()
