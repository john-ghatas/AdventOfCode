#!/usr/bin/python
y, x, treecount = 0, 0, 0
steps = []

tree_stream = open('tree.txt', 'r')
tree = tree_stream.readlines()
max_x = len(tree[0])
max_y = 0

for branch in tree:
    x = (x + 3) % (len(branch) - 1)
    steps.append(x)
    max_y += 1

for i in range(max_y):
    if i == max_y - 1:
        break

    if tree[i + 1][steps[i]] == '#':
        treecount += 1

print(treecount)
