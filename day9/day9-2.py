from itertools import pairwise

from day9 import read_input


def solver(nums):
    diff = [y - x for x, y in pairwise(nums)]
    res = [diff[0]]
    while any(i != 0 for i in diff):
        diff = [y - x for x, y in pairwise(diff)]
        res.append(diff[0])
    while len(res) > 1:
        x = res.pop(-1)
        y = res.pop(-1)
        res.append(y-x)
    return nums[0] - res[0]


def main(nums):
    return sum([solver(num) for num in nums])


if __name__ == '__main__':
    assert solver([0, 3, 6, 9, 12, 15]) == -3
    assert solver([1, 3, 6, 10, 15, 21]) == 0
    assert solver([10, 13, 16, 21, 30, 45]) == 5
    print(main(read_input()))
