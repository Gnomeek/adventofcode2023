from functools import reduce
from typing import List, Dict, Tuple

from day2 import read_input


def solver(picks: List[Dict[str, int]]) -> Tuple[int, int, int]:
    return (
        max([i.get("red", float('-inf')) for i in picks]),
        max([i.get("green", float('-inf')) for i in picks]),
        max([i.get("blue", float('-inf')) for i in picks]),
    )


def main():
    result = 0
    for line in read_input():
        res = solver(line)
        result += reduce(lambda x, y: x * y, res)
    print(result)


if __name__ == '__main__':
    main()
