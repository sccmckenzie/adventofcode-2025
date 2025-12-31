path = 'input.csv'

with open(path) as f:
    # read each line into a list of int lists
    banks = [[int(digit) for digit in line if digit.isdigit()] for line in f]

def find_earliest_max(int_list: list[int], offset: int = 0) -> int:
    # apply offset, producing a smaller list of eligible int
    # in this puzzle, offset is necessary to ensure we have enough remaining choices
    # e.g. if you have to select 12 batteries, your first choice cannot be index 11
    end_index = len(int_list) - offset + 1
    eligible_int = int_list[0:end_index]

    earliest_max = max(eligible_int)
    del int_list[0:eligible_int.index(earliest_max) + 1]

    return earliest_max

total_output_joltage = 0

for bank in banks:
    # bank_input to stay unaltered for reference TODO: might not need this
    bank_input = bank.copy()
    batteries_to_enable = list()
    for num_batteries_outstanding in range(12, 0, -1):
        # this function pops the earliest max
        # while also removing all preceding entries
        # index is required to determine eligible entries
        batteries_to_enable.append(find_earliest_max(bank, num_batteries_outstanding))

    total_output_joltage += int("".join([str(digit) for digit in batteries_to_enable]))

print(total_output_joltage)