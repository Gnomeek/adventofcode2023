digits = [str(i) for i in range(10)]
spelled_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
def solver(line: str) -> int:
    tmp, line = "", unify_str(line)
    for i in line:
        if i in digits:
            tmp += i
            break
    for i in line[::-1]:
        if i in digits:
            tmp += i
            break
    return int(tmp)

def unify_str(line: str) -> str:
    for spelled, digit in spelled_digits.items():
        line = line.replace(spelled, spelled+digit+spelled)

    return line

def main():
    res = 0
    with open("input.txt") as f:
        for l in f:
            res += solver(l)
    print(res)

if __name__ == '__main__':
    main()