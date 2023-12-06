def read_input():
    res = []
    with open("input.txt") as f:
        for line in f:
            cleared = line.split(":")[1].strip()
            winnings, picks = cleared.split("|")
            winnings, picks = winnings.strip().split(" "), picks.strip().split(" ")
            winnings, picks = list(filter(lambda a: a != "", winnings)), list(filter(lambda a: a != "", picks))
            res.append((winnings, picks))
        return res
