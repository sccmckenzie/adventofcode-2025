import numpy as np

path = 'input.txt'

available_ingredients = []
fresh_ranges = []

with open(path) as f:
    # read each line
    # note we intentionally keep dtype as string, we'll let numpy parse as uint laer
    for line in f:
        if len(line.strip()) == 0:
            continue
        elif '-' in line:
            fresh_ranges.append(line.strip().split('-'))
        else:
            available_ingredients.append(line.strip())

available_ingredients = np.array(available_ingredients, dtype='int64')
fresh_ranges = np.array(fresh_ranges, dtype='int64')
# sorting is particularly useful for Part 2
fresh_ranges.sort(axis=0)

lower = available_ingredients[:,None] >= fresh_ranges[:,0]
upper = available_ingredients[:,None] <= fresh_ranges[:,1]

# Part 1
print(len(available_ingredients[(lower & upper).any(1)]))

# Part 2
fresh_ranges_dedupe = fresh_ranges.copy()
overlap_mask = fresh_ranges_dedupe[:-1, 1] >= fresh_ranges_dedupe[1:, 0]

fresh_ranges_dedupe[:-1,1][overlap_mask] = fresh_ranges_dedupe[1:,0][overlap_mask] - 1

np.sum(fresh_ranges_dedupe[:,1] - fresh_ranges_dedupe[:,0] + 1)

