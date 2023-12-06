from typing import List, Dict


def read_input() -> List[List[Dict[str, int]]]:
    res = []
    with open("input.txt") as f:
        for l in f:
            picks = l.replace(" ", "").replace("\n", "").split(":")[1].split(";")
            tmp = []
            for pick in picks:
                tmp_dict = {}
                balls = pick.split(",")
                for ball in balls:
                    num, color, c = "", "", 0
                    while c < len(ball):
                        if ball[c].isnumeric():
                            num += ball[c]
                            c += 1
                        else:
                            color = ball[c:]
                            break
                    tmp_dict[color] = int(num)
                tmp.append(tmp_dict)
            res.append(tmp)
    return res