import re

def split_file_on_empty_line(file_path):
    before_empty = []  # Lines before the empty line
    after_empty = []   # Lines after the empty line
    found_empty_line = False  # Flag to track when the empty line is found

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace

            if line == "" and not found_empty_line:
                found_empty_line = True  # The empty line is found, start reading after it
                continue  # Skip the empty line itself
            
            if not found_empty_line:
                before_empty.append(line)  # Lines before the empty line
            else:
                after_empty.append(line)   # Lines after the empty line

    return before_empty, after_empty

def check_order(before_empty, after_empty):
    # Parse the before_empty list into pairs of integers
    before_pairs = [tuple(map(int, line.split('|'))) for line in before_empty]

    valid_lines = []  # List to store valid lines
    invalid_lines = []  # List to store valid lines

    # Check each line in after_empty
    for line in after_empty:
        # Parse the line into a list of numbers (comma-separated)
        after_numbers = list(map(int, line.split(',')))

        # Assume the line is valid until proven otherwise
        is_valid = True

        # Compare each number with all numbers that come after it in the list
        for i in range(len(after_numbers)):
            for j in range(i + 1, len(after_numbers)):  # Compare current number with all subsequent numbers
                num1 = after_numbers[i]
                num2 = after_numbers[j]

                # If the pair (num1, num2) exists in before_pairs
                if (num1, num2) in before_pairs:
                    is_valid = True
                # If the pair (num2, num1) exists in before_pairs, it means num2 should come before num1
                elif (num2, num1) in before_pairs:
                    is_valid = False
                    break  # No need to check further, this line is invalid

            if not is_valid:
                invalid_lines.append(line)
                break  # If any invalid order found, stop checking the rest of the numbers

        # If the line is valid, add it to valid_lines
        if is_valid:
            valid_lines.append(line)

    return valid_lines, invalid_lines

# Usage
file_path = 'input.txt'
before_empty, after_empty = split_file_on_empty_line(file_path)

# Get the valid lines that meet the order rules
valid_lines, invalid_lines = check_order(before_empty, after_empty)

total = 0
# Output valid lines
if valid_lines:
    print("Valid lines in after_empty:")
    for valid_line in valid_lines:
        print(valid_line)
        after_numbers = list(map(int, valid_line.split(',')))
        print(after_numbers[len(after_numbers) // 2])
        total += (after_numbers[len(after_numbers) // 2])
else:
    print("No valid lines in after_empty.")
    
print (total)
