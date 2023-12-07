from day5 import read_input, solver


def main():
    seeds, mappings = read_input()
    return min([solver(seed, mappings) for seed in seeds])

if __name__ == '__main__':
    print(main())
