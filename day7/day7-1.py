from collections import Counter


def read_input():
    res = []
    with open("input.txt") as f:
        for l in f:
            res.append(l.strip().split(" "))
    return res


def strength(hand):
    c = Counter(hand)
    if 5 in c.values():
        return 7
    elif 4 in c.values():
        return 6
    elif list(c.values()).count(2) == 1 and list(c.values()).count(3) == 1:
        return 5
    elif list(c.values()).count(1) == 2 and list(c.values()).count(3) == 1:
        return 4
    elif list(c.values()).count(2) == 2:
        return 3
    elif list(c.values()).count(2) == 1 and list(c.values()).count(1) == 3:
        return 2
    return 1


def easy_sort(hand, bid):
    return strength(hand), *map("23456789TJQKA".index, hand), bid


def solver(stdin):
    t = sorted(easy_sort(h, int(b)) for h, b in stdin)
    return sum(rank*bid for rank, (*_, bid) in enumerate(t,1))


if __name__ == '__main__':
    print(solver(read_input()))