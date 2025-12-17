class Dial:
    def __init__(self, starting_number):
        self.number = starting_number
        self.num_landed_zero = 0
        self.num_crossed_zero = 0

    def turn(self, direction, distance):
        new_number = self.number

        if direction == 'R':
            new_number += distance
        elif direction == 'L':
            new_number -= distance

        # if starting from 0
        if self.number == 0:
            # any negative new_number is going to show at least ONE cross
            # we need to subtract one if starting from zero, unless it's -100
            if new_number < 0:
                # if new_number multiple of 100
                if new_number % 100 == 0:
                    self.num_crossed_zero += abs(new_number // 100)
                else:
                    self.num_crossed_zero += abs(new_number // 100) - 1
            # positive crosses will be reported normally
            else:
                self.num_crossed_zero += new_number // 100
        # or, it might just LAND on zero (unnormalized)
        elif new_number == 0:
            self.num_crossed_zero += 1
        # the normal case, starting from 1-99
        else:
            self.num_crossed_zero += abs(new_number // 100)


        if new_number % 100 == 0:
            self.num_landed_zero += 1

        self.number = new_number % 100

        return self

class Turn:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = distance

def read_file_to_dict(file_path):
    """
    Reads a file line by line into a dictionary,
    where each line number (1-indexed) is the key and the line content is the value.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary with line numbers as keys and line content as values.
    """
    line_dict = {}
    try:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file, 1):
                line_dict[i] = line.strip('\n') # Store the line, stripping only the newline character
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return line_dict

def parse_turn_string(turn_string: str) -> Turn:
    """
    Parses a turn string like 'L68' into a Turn object.

    Args:
        turn_string (str): The string to parse.

    Returns:
        Turn: A Turn object with direction and distance.
    """
    direction = turn_string[0]
    distance = int(turn_string[1:])
    return Turn(direction, distance)

if __name__ == "__main__":
    file_path = 'input.csv'
    file_content_dict = read_file_to_dict(file_path)

    if file_content_dict:
        print(f"Content of '{file_path}' loaded into dictionary:")
        
        dial = Dial(starting_number=50) # Initialize the dial

        num_zero = 0

        for line_num, content in file_content_dict.items():
            turn = parse_turn_string(content)
            dial.turn(turn.direction, turn.distance)

        print(f"\nFinal dial number: {dial.number}")
        print(f"\nNumber of times @ zero: {dial.num_landed_zero}")
        print(f"\nNumber of times crossed zero: {dial.num_crossed_zero}")