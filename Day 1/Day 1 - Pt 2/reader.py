#!/usr/bin/python
import sys
import numpy
import resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**6)
# Define functions here


def find3Numbers(A, arr_size, sum):
    A.sort()
    for i in range(0, arr_size-2):
        l = i + 1
        r = arr_size-1
        while (l < r):

            if(A[i] + A[l] + A[r] == sum):
                print(
                    f"The sum of the triplet {[A[i], A[l], A[r]]} is {numpy.prod([A[i], A[l], A[r]])}")
                return True

            elif (A[i] + A[l] + A[r] < sum):
                l += 1
            else:
                r -= 1
    return False
    # Pulled from https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/


# Read file and dump all lines
numbers = open('../numbers.txt', 'r')
all_numbers = numbers.readlines()
parsed_numbers = []

# Prase the lines and put them in an array
for number in all_numbers:
    parsed_numbers.append(int(number))

max_index = len(parsed_numbers)


find3Numbers(parsed_numbers, len(parsed_numbers), 2020)
