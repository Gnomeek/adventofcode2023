def read_input():
    res = []
    with open("input.txt") as f:
        for i in f:
            res.append([int(num) for num in i.strip().split(" ")])
    return res