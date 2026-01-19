import numpy as np
import re

path = 'input.txt'

# part 1
with open(path) as f:
    lines = [re.split('\\s+', line.strip()) for line in f]

ops = np.array(lines[-1])
num_array = np.array(lines[:-1], dtype='uint64')
answers1 = np.where(ops == '*', num_array.prod(axis=0), num_array.sum(axis=0))

np.sum(answers1)

# part 2
with open(path) as f:
    lines = [line.replace('\n', '') for line in f][0:-1]

str_array = np.array(lines)

max_len = np.strings.str_len(str_array).max()

# need to standardize all lines to same len so we can form even array of elements
str_array = np.strings.ljust(str_array, max_len, ' ')

# split out into elements
str_array = np.array([list(row) for row in str_array], dtype=object)

# stich new numbers together vertically, starting from the top down
reduced = np.strings.strip(np.add.reduce(str_array, axis=0).astype('str_'))

# group elements by "column"
mask = np.strings.isdigit(reduced)
rearranged = np.split(reduced, np.where(~mask)[0])
rearranged_casted = [elements[elements != ''].astype('uint16') for elements in rearranged]

# calculate the results for each group
result_sums = [elements.sum() for elements in rearranged_casted]
result_products = [elements.prod() for elements in rearranged_casted]

np.where(ops == '*', result_products, result_sums).sum()