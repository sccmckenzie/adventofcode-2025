class Dial:
    def __init__(self, starting_number):
        self.number = starting_number
        self.num_landed_zero = 0
        self.num_crossed_zero = 0

    def click(self, direction):
        """
            Move the dial just one "click"
        """
        if direction == 'L':
            if self.number == 0:
                self.number = 99
            else:
                self.number -= 1
        elif direction == 'R':
            if self.number == 99:
                self.number = 0
            else:
                self.number += 1
        else:
            raise ValueError('Invalid direction')

        return self

    def turn(self, direction, distance):

        while (distance > 0):
            if direction == 'L':
                self.click('L')
                distance -= 1
            elif direction == 'R':
                self.click('R')
                distance -= 1
            if self.number == 0:
                self.num_crossed_zero += 1

        if self.number == 0:
            self.num_landed_zero += 1

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
    input_file = 'input.csv'
    file_content_dict = read_file_to_dict(input_file)

    if file_content_dict:
        print(f"Content of '{input_file}' loaded into dictionary:")
        
        dial = Dial(starting_number=50) # Initialize the dial

        num_zero = 0

        for line_num, content in file_content_dict.items():
            turn = parse_turn_string(content)
            dial.turn(turn.direction, turn.distance)

        print(f"\nFinal dial number: {dial.number}")
        print(f"\nNumber of times @ zero: {dial.num_landed_zero}")
        print(f"\nNumber of times crossed zero: {dial.num_crossed_zero}")