from functools import reduce


def solver(zipped):
    res = []
    for t, d in zipped:
        solutions = [i * (t - i) for i in range(t)]
        res.append(len([i for i in solutions if i > d]))
    print(res)
    return reduce(lambda x, y: x * y, res)
