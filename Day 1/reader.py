#!/usr/bin/python
import sys
import gc
import time
# Define functions here


def parse_array(base, index, numbers_list, max_index, iter=0):
    if(iter % 2000 == 0):
        gc.collect()

    if(index >= max_index - 2):
        base = base + 1
        index = base

    if(base > max_index - 1):
        return False

    current_base = numbers_list[base]
    current_index = numbers_list[index]
    current_third_num = numbers_list[index + 1]
    current_sum = sum([current_base, current_index, current_third_num])

    if(current_sum == 2020):
        print(f"Needed {iter} amount of iterations")
        print(
            f"The sum of {current_base} and {current_index} and {current_third_num} equal to 2020. Multiplying these numbers results in {current_base * current_index * current_third_num}")
        return True

    parse_array(base, index + 1, numbers_list, max_index, iter + 1)


# Read file and dump all lines
numbers = open('numbers.txt', 'r')
all_numbers = numbers.readlines()
parsed_numbers = []

# Prase the lines and put them in an array
for number in all_numbers:
    parsed_numbers.append(int(number))

max_index = len(parsed_numbers)
sys.setrecursionlimit(max_index ** 2)

parse_array(0, 1, parsed_numbers, max_index)
