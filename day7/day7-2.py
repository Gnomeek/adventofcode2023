from collections import Counter


def read_input_2():
    res = []
    with open("input.txt") as f:
        for l in f:
            l = l.replace("J", "*")
            res.append(l.strip().split(" "))
    return res


def strength_2(hand):
    c = Counter(hand)
    counts = [0] if (jokers := c.pop("*", 0)) == 5 else sorted(c.values())
    # The most efficient use of a joker is always as the most common non-joker card
    counts[-1] += jokers
    match counts:
        case *_, 5:
            return 7
        case *_, 4:
            return 6
        case *_, 2, 3:
            return 5
        case *_, 3:
            return 4
        case *_, 2, 2:
            return 3
        case *_, 2:
            return 2
    return 1


def easy_sort(hand, bid):
    return strength_2(hand), *map("*23456789TJQKA".index, hand), bid


def solver(stdin):
    t = sorted(easy_sort(h, int(b)) for h, b in stdin)
    return sum(rank*bid for rank, (*_, bid) in enumerate(t,1))


if __name__ == '__main__':
    print(solver(read_input_2()))