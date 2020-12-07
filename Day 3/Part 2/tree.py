#!/usr/bin/python
import numpy


def traverse_slopes(increment_x, increment_y):
    y, x, treecount = 0, 0, 0
    steps = []
    max_y = 0

    for i in range(int(len(slope) / increment_y)):
        x = (x + increment_x) % (len(slope[i]) - 1)
        steps.append(x)
        max_y += 1

    for step in steps:
        if y == max_y - increment_y:
            break

        if slope[y + increment_y][step] == '#':
            treecount += 1

        y += increment_y
    print(
        f"Finished calculating the trajectory for an increment sideways of {increment_x} and downwards of {increment_y}. A total of {treecount} have been found in the way!")
    return treecount


slope_stream = open('../tree.txt', 'r')
slope = slope_stream.readlines()

total_slopes = [traverse_slopes(1, 1), traverse_slopes(3, 1), traverse_slopes(
    5, 1), traverse_slopes(7, 1), traverse_slopes(1, 2)]

print(numpy.product(total_slopes))
