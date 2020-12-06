#!/usr/bin/python
import sys

# Define functions here


def parse_array(base, index, numbers_list, max_index, iter=0):
    if(base > max_index - 1):
        return False

    if(index >= max_index - 1):
        base = base + 1
        index = base

    current_base = numbers_list[base]
    current_index = numbers_list[index]
    current_sum = current_base + current_index

    if(current_sum == 2020):
        print(f"Needed {iter} amount of iterations")
        print(
            f"The sum of {current_base} and {current_index} equal to 2020. Multiplying these numbers results in {current_base * current_index}")
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
