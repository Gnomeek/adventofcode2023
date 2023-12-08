from collections import OrderedDict


def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        instructions = lines[0].strip()
        memo = OrderedDict()
        for i in lines[2:]:
            k, v = i.split("=")
            k = k.strip()
            v = [i.strip() for i in v.replace("(", "").replace(")", "").strip().split(", ")]
            memo[k] = v
        return instructions, memo
