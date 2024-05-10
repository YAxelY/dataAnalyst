def parse_input_string(input_string):
    # Split the input string into rows
    rows = input_string.split("\n")
    # Initialize an empty list to store the result
    result = []
    # Iterate over each row
    for row in rows:
        # Split the row by spaces to extract individual numbers
        numbers = row.split()
        # Convert the numbers from strings to floating-point numbers
        numbers = [float(num) for num in numbers]
        # Append the numbers to the result list
        result.append(numbers)
    return result


def parse_input_stringr(inputString):
    # Split the input string into rows
    rows = inputString.split("\n")
    # Initialize an empty list to store the result
    result = []
    # Iterate over each row
    for row in rows:
        # Check if the row contains commas
        if "," in row:
            # Split the row by commas to extract individual numbers
            numbers = row.split(",")
        else:
            # Split the row by spaces to extract individual numbers
            numbers = row.split()
        # Convert the numbers from strings to floating-point numbers
        numbers = [float(num) for num in numbers]
        # Append the numbers to the result list
        result.append(numbers)
    return result




def max_digit_number(numbers):
    max_digit = -1
    number_with_max_digit = None

    for number in numbers:
        # Convert the number to a string to iterate through its digits
        str_number = str(number)
        
        # Iterate through each digit in the number
        for digit_char in str_number:
            digit = int(digit_char)
            
            # Update max_digit if we find a higher digit
            if digit > max_digit:
                max_digit = digit
                number_with_max_digit = number
            elif digit == max_digit and number > number_with_max_digit:
                # If the current number has the same highest digit, but is larger,
                # update the number_with_max_digit
                number_with_max_digit = number
    
    return number_with_max_digit


def get_entry_values(entry_widgets):
    entry_values = []
    for entry in entry_widgets:
        entry_values += [entry.get()]
    return entry_values

def get_entry_valuesd(entryWidgetsDict):
    entryValues = list(entryWidgetsDict.values())
    entryv = []
    for entry in entryValues:
        entryv +=[entry.get()]
    return entryv