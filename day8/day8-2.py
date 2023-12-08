from math import lcm

from day8 import read_input


def solver(instructions, memo, cur):
    cnt = 0
    instructions *= 100000
    while cnt < len(instructions):
        if instructions[cnt] == "L":
            cur = memo[cur][0]
        else:
            cur = memo[cur][1]
        if cur[-1] == "Z":
            return cnt + 1
        cnt += 1


if __name__ == '__main__':
    instructions, memo = read_input()
    starts = [i for i in memo.keys() if i[-1] == "A"]
    res = []
    for i in starts:
        res.append(solver(instructions, memo, i))
    print(lcm(*res))