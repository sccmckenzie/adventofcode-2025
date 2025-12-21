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

def collect_invalid(range_dict):
    invalid_num_list = []

    for range_spec in range_dict.values():
        for num in range(range_spec['lo'], range_spec['hi'] + 1, 1):
            num_str = str(num)
            # if num is even
            if len(num_str) % 2 == 0:
                # Calculate midpoint
                mid = len(num_str) // 2

                # Slice from start to mid, and mid to end
                left = num_str[:mid]
                right = num_str[mid:]

                if left == right:
                    invalid_num_list.append(num)

    return invalid_num_list

if __name__ == "__main__":
    file_path = 'input.txt'
    product_ranges = read_file_to_dict(file_path)

    invalid_num = collect_invalid(product_ranges)

    print(invalid_num)
    print(sum(invalid_num))
