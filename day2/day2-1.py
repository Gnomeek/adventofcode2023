from typing import List, Dict

from day2 import read_input

RED, GREEN, BLUE = 12, 13, 14

def solver(picks: List[Dict[str, int]]):
    if any([i.get("red", 0) > RED for i in picks]):
        return False
    if any([i.get("green", 0) > GREEN for i in picks]):
        return False
    if any([i.get("blue", 0) > BLUE for i in picks]):
        return False
    return True

def main():
    result = 0
    for idx, line in enumerate(read_input()):
        result += idx + 1 if solver(line) else 0
    print(result)


if __name__ == '__main__':
    main()