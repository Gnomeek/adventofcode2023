import sys
import numpy as np
from collections import defaultdict
from pprint import pprint


def read_file(path):
    with open(path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def to_array(lines):
    arr = np.array([list(line) for line in lines])
    print(arr)
    return arr


def check_for_symbol(arr, row, col):
    check_dict = {
        'up_left': (row - 1, col - 1),
        'up_mid': (row - 1, col),
        'up_right': (row - 1, col + 1),
        'mid_left': (row, col - 1),
        'mid_right': (row, col + 1),
        'lo_left': (row + 1, col - 1),
        'lo_mid': (row + 1, col),
        'lo_right': (row + 1, col + 1),
    }

    for direction, checkcoords in check_dict.items():
        if (checkcoords[0] < 0) or (checkcoords[0] > arr.shape[0] - 1):
            continue
        if (checkcoords[1] < 0) or (checkcoords[1] > arr.shape[1] - 1):
            continue

        if not arr[checkcoords].isalnum() and (arr[checkcoords] != '.'):
            return True
    return False


def calculate(array):
    valid_nums = defaultdict(list)
    for row in range(array.shape[0]):
        curr_num = ''
        VALID = False
        for col in range(array.shape[1]):
            curr_symbol = array[row, col]
            if curr_symbol.isdigit():
                if check_for_symbol(arr=array, row=row, col=col):
                    VALID = True
                    curr_num += curr_symbol
                else:
                    curr_num += curr_symbol
            elif not curr_symbol.isdigit():
                if curr_num:
                    if VALID:
                        VALID = False
                        valid_nums['valid'].append(int(curr_num))
                        curr_num = ''
                    else:
                        VALID = False
                        valid_nums['invalid'].append(int(curr_num))
                        curr_num = ''
                else:
                    VALID = False
                    curr_num = ''
            # Handle EO Line Numbers
            if col == (array.shape[1] - 1):
                if curr_num:
                    if VALID:
                        VALID = False
                        valid_nums['valid'].append(int(curr_num))
                        curr_num = ''
                    else:
                        VALID = False
                        valid_nums['invalid'].append(int(curr_num))
                        curr_num = ''
                else:
                    VALID = False
                    curr_num = ''

    pprint(valid_nums)
    return sum(valid_nums['valid'])


def main(file):
    lines = read_file(file)
    array = to_array(lines)
    result = calculate(array)

    return result


if __name__ == '__main__':
    result = main("input.txt")
    print(result)
