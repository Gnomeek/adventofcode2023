from itertools import pairwise

from day9 import read_input


def solver(nums):
    diff = [y - x for x, y in pairwise(nums)]
    res = [nums[-1], diff[-1]]
    while any(i != 0 for i in diff):
        diff = [y - x for x, y in pairwise(diff)]
        res.append(diff[-1])
    return sum(res)


def main(nums):
    return sum([solver(num) for num in nums])


if __name__ == '__main__':
    assert solver([0, 3, 6, 9, 12, 15]) == 18
    assert solver([1, 3, 6, 10, 15, 21]) == 28
    assert solver([10, 13, 16, 21, 30, 45]) == 68
    print(main(read_input()))
