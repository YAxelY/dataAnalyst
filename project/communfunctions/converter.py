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