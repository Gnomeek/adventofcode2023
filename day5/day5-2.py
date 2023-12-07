import time

from day5 import read_input

def gen_real_seeds(seeds):
    res = []
    for i in range(0, len(seeds), 2):
        res.append((seeds[i], seeds[i]+seeds[i+1]))
    res = merge_ranges(res)
    return res


def merge_ranges(ranges):
    # Sort the ranges based on the start value
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    merged_ranges = []
    current_range = sorted_ranges[0]

    for start, end in sorted_ranges[1:]:
        if start <= current_range[1]:  # Overlapping ranges
            current_range = (current_range[0], max(current_range[1], end))
        else:
            merged_ranges.append(current_range)
            current_range = (start, end)

    merged_ranges.append(current_range)
    return merged_ranges


def main():
    seeds, mappings = read_input()
    candidates = [[] for _ in range(len(mappings.values()))]
    start = time.time()
    for r_start, r_end in gen_real_seeds(seeds):
        ranges = [(r_start, r_end)]
        for i, mapping in enumerate(mappings.values()):
            while ranges:
                r_start, r_end = ranges.pop()
                for desc_start, src_start, length in mapping:
                    src_end = src_start + length
                    offset = desc_start - src_start
                    if src_end <= r_start or r_end <= src_start:
                        continue
                    if r_start < src_start:
                        ranges.append((r_start, src_start))
                        r_start = src_start
                    if src_end < r_end:
                        ranges.append((src_end, r_end))
                        r_end = src_end
                    r_start += offset
                    r_end += offset
                    break
                candidates[i].append((r_start, r_end))
            ranges = candidates[i]
    print(time.time()-start)
    return min(candidates[-1])[0]


if __name__ == '__main__':
    print(main())
