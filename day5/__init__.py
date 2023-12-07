from collections import OrderedDict

def solver(seed, mappings):
    target = seed
    for _, v in mappings.items():
        for row in v:
            if row[1] <= target <= (row[1] + row[2]):
                target = row[0] + target - row[1]
                break
    return target

def read_input():
    seeds = []
    mappings = OrderedDict({
        "seed_to_soil": [],
        "soil_to_fertilizer": [],
        "fertilizer_to_water": [],
        "water_to_light": [],
        "light_to_temperature": [],
        "temperature_to_humidity": [],
        "humidity_to_location": [],
    })
    with open("input.txt") as f:
        lines, l = f.readlines(), 0
        while l < len(lines):
            if lines[l].startswith("seeds:"):
                seeds = [int(i) for i in lines[l].split(":")[1].strip().split(" ")]
            if lines[l].startswith("seed-to-soil"):
                l += 1
                while lines[l].strip() != "":
                    mappings["seed_to_soil"].append([int(i) for i in lines[l].strip().split(" ")])
                    l += 1
            if lines[l].startswith("soil-to-fertilizer"):
                l += 1
                while lines[l].strip() != "":
                    mappings["soil_to_fertilizer"].append([int(i) for i in lines[l].strip().split(" ")])
                    l += 1
            if lines[l].startswith("fertilizer-to-water"):
                l += 1
                while lines[l].strip() != "":
                    mappings["fertilizer_to_water"].append([int(i) for i in lines[l].strip().split(" ")])
                    l += 1
            if lines[l].startswith("water-to-light"):
                l += 1
                while lines[l].strip() != "":
                    mappings["water_to_light"].append([int(i) for i in lines[l].strip().split(" ")])
                    l += 1
            if lines[l].startswith("light-to-temperature"):
                l += 1
                while lines[l].strip() != "":
                    mappings["light_to_temperature"].append([int(i) for i in lines[l].strip().split(" ")])
                    l += 1
            if lines[l].startswith("temperature-to-humidity"):
                l += 1
                while lines[l].strip() != "":
                    mappings["temperature_to_humidity"].append([int(i) for i in lines[l].strip().split(" ")])
                    l += 1
            if lines[l].startswith("humidity-to-location"):
                l += 1
                while l < len(lines) and lines[l].strip() != "":
                    mappings["humidity_to_location"].append([int(i) for i in lines[l].strip().split(" ")])
                    l += 1
            l += 1
    return seeds, mappings