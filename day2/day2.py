def read_file_to_dict(file_path):
    """
    Reads a comma-separated line into a dictionary,

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary with line numbers as keys and line content as values.
    """
    try:
        with open(file_path, 'r') as f:
            raw_line = f.readline()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    raw_dict = {i: val for i, val in enumerate(raw_line.split(','))}
    range_dict = {}

    # Loop through and transform
    for key, value in raw_dict.items():
        # Split the string by the hyphen
        low_val, hi_val = value.split('-')

        range_dict[key] = {
            'lo': int(low_val),
            'hi': int(hi_val)
        }

    return range_dict

def collect_repeats(range_dict) -> set[int]:
    repeat_num_list = []

    for range_spec in range_dict.values():
        # iterate through each range_spec
        for num in range(range_spec['lo'], range_spec['hi'] + 1, 1):
            # we are analyzing the string, not the number itself...
            num_str = str(num)
            len_num = len(num_str)

            # what is the highest divisor for len_num?
            max_divisor = len_num // 2

            # which integers nicely fit into len_num?
            divisor_fit_list = []
            for divisor in range(1, max_divisor + 1):
                if len_num % divisor == 0:
                    divisor_fit_list.append(divisor)

            # for each divisor in divisor_fit_list, are the corresponding quotient groups identical?
            for divisor in divisor_fit_list:
                quotient_groups = []
                # carve up string into quotient gruops, length devisor
                for d in range(divisor, len_num + divisor, divisor):
                    quotient_groups.append(num_str[(d - divisor):(d)])

                # are the elements of quotient_groups identical?
                if len(set(quotient_groups)) == 1:
                    repeat_num_list.append(num)

    repeat_num_set = set(repeat_num_list)
    return set(repeat_num_set)

if __name__ == "__main__":
    input_file = 'input.txt'
    product_ranges = read_file_to_dict(input_file)

    invalid_num = collect_repeats(product_ranges)

    print(invalid_num)
    print(sum(invalid_num))
