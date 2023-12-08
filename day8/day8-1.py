from day8 import read_input

def solver(instructions, memo):
    cnt, cur = 0, "AAA"
    instructions *= 100000
    while cnt < len(instructions):
        if instructions[cnt] == "L":
            cur = memo[cur][0]
        else:
            cur = memo[cur][1]
        if cur == "ZZZ":
            return cnt + 1
        cnt += 1

if __name__ == '__main__':
    x = solver(*read_input())
    print(x)