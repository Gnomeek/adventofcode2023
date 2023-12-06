import sys
import numpy as np
from collections import defaultdict
from pprint import pprint


def read_file(path):
    ''' read files line by line'''
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

        if arr[checkcoords] == '*':
            return True, '-'.join(str(i) for i in checkcoords)
    return False, '0-0'


def calculate(array):
    ''' do stuff'''
    valid_nums = defaultdict(list)
    valid_nums2 = {'valid': defaultdict(list), 'invalid': defaultdict}
    for row in range(array.shape[0]):
        curr_num = ''
        VALID = False
        VALID_SYM_COORDS = '0-0'
        for col in range(array.shape[1]):
            curr_symbol = array[row, col]
            if curr_symbol.isdigit():
                check, sym_coords = check_for_symbol(arr=array, row=row, col=col)
                if check:
                    VALID = True
                    curr_num += curr_symbol
                    VALID_SYM_COORDS = sym_coords
                else:
                    curr_num += curr_symbol
            elif not curr_symbol.isdigit():
                if curr_num:
                    if VALID:
                        VALID = False
                        valid_nums['valid'].append(int(curr_num))
                        valid_nums2['valid'][VALID_SYM_COORDS].append(int(curr_num))
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
                        valid_nums2['valid'][VALID_SYM_COORDS].append(int(curr_num))
                        curr_num = ''
                    else:
                        VALID = False
                        valid_nums['invalid'].append(int(curr_num))
                        curr_num = ''
                else:
                    VALID = False
                    curr_num = ''

    # pprint(valid_nums)
    # pprint(valid_nums2)

    return sum(np.product(vals) for vals in valid_nums2['valid'].values() if len(vals) == 2)


def main(file):
    lines = read_file(file)
    array = to_array(lines)
    result = calculate(array)

    return result


if __name__ == '__main__':
    result = main("input.txt")
    print(result)
