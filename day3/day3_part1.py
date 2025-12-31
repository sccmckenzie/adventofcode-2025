path = 'input.csv'

with open(path) as f:
    # read each line into a list of int lists
    banks = [[int(digit) for digit in line if digit.isdigit()] for line in f]

def find_earliest_max_index(int_list, allow_last=True):
    if not allow_last:
        # when selecting first battery, last battery isn't an option...
        # ...bc there will not be any remaining choices!
        int_list = int_list[:-1]

    return int_list.index(max(int_list))

total_output_joltage = 0


for bank in banks:
    first_battery_index = find_earliest_max_index(bank, allow_last=False)
    second_battery_index = find_earliest_max_index(bank[first_battery_index + 1:]) + first_battery_index + 1
    total_output_joltage += int(str(bank[first_battery_index]) + str(bank[second_battery_index]))

print(total_output_joltage)