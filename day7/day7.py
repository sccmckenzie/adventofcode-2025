import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

np.set_printoptions(linewidth=100)

input_path = 'input.csv'

diagram = np.genfromtxt(input_path, dtype='str_', delimiter=1)
# create path tally array (see path_tally_demo.txt)
tally = np.zeros_like(diagram, dtype='uint64')
# initialize first row with 1 coinciding w tachyon beam start
tally[0][diagram[0] == 'S'] = 1

diagram_slides = sliding_window_view(diagram, axis=0, window_shape=2, writeable=True).swapaxes(1, 2)
tally_slides = sliding_window_view(tally, axis=0, window_shape=2, writeable=True).swapaxes(1, 2)

num_splits = 0

for dslide, tslide in zip(diagram_slides, tally_slides):
    # straight trajectory
    straights = np.logical_and(np.isin(dslide[0], ['S', '|']), dslide[1] == '.')
    dslide[1] = np.where(straights, '|', dslide[1])
    tslide[1] = np.where(straights, tslide[0], tslide[1])

    # split
    # step 1: identify index of struck splitters
    struck = np.logical_and(np.isin(dslide[0], ['S', '|']), dslide[1] == '^')

    num_splits += struck.sum()

    # step 2: create offset arrays to set neighboring elements to '|'
    dleft = np.pad(struck[1:], (0, 1), constant_values=False)
    dright = np.pad(struck[:-1], (1, 0), constant_values=False)
    dadjacent = (dleft | dright)
    dslide[1][dadjacent] = '|'

    # step 3: identify struck quantities
    struck_qty = np.where(struck, tslide[0], 0)

    # step 4: cascade struck quantities to next row
    tleft = np.pad(struck_qty[1:], (0, 1), constant_values=False)
    tright = np.pad(struck_qty[:-1], (1, 0), constant_values=False)
    ttotal = tleft + tright
    tslide[1] = np.where(dadjacent, tslide[1] + ttotal, tslide[1])

# calculate num of timelines
num_timelines = tally[-1].sum(axis=0)

# pretty print diagram
for row in diagram:
    print("".join(item.rjust(2) for item in row))

# pretty print diagram interlaced w tally
cell_width = np.strings.str_len(tally.astype('str_')).max() + 1
interlaced = np.empty((tally.shape[0] + diagram.shape[0], diagram.shape[1]), dtype=f'U{cell_width}')
interlaced[0::2] = diagram
interlaced[1::2] = tally.astype('str_')

for row in interlaced:
    # rjust(max_width) aligns to the right, ljust(max_width) to the left
    print("".join(item.rjust(cell_width) for item in row))

# np.savetxt('output.csv', diagram, fmt='%s', delimiter='')

# Part 1
print(num_splits)

# Part 2
print(num_timelines)