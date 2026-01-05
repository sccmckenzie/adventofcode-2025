import numpy as np

path = 'input.txt'

def parse_character(x: str) -> int:
    if x == '@':
        return 1
    elif x == '.':
        return 0
    else:
        raise ValueError

def find_accessible_rolls(input_grid) -> int:
    height = input_grid.shape[0] - 2
    width = input_grid.shape[0] - 2

    # we will slowly populate value 1 @ indices satisfying "less than 3 neighbors" condition in input_grid
    accessible_only = np.zeros_like(input_grid, dtype=bool)

    for i in range(1, 1 + height, 1):
        for j in range(1, 1 + width, 1):
            center_element = grid[i, j]
            if center_element:
                total_sum = grid[i - 1:i + 2, j - 1:j + 2].sum()
                neighbor_sum = total_sum - center_element
                if neighbor_sum < 4:
                    accessible_only[i, j] = True
            else:
                continue

    # this represents "removing" the accessible rolls
    input_grid[accessible_only] = 0

    return accessible_only.sum()

with open(path) as f:
    # read each line
    lines = [[parse_character(char) for char in line.strip()] for line in f]

grid_raw = np.array(lines)
grid = np.pad(grid_raw, pad_width=1, mode='constant', constant_values='0')

cum_accessible = 0

while True:
    new_accessible = find_accessible_rolls(grid)
    cum_accessible += new_accessible
    if new_accessible == 0:
        break

print(cum_accessible)

