# Prompt the user to input a 3-digit number
number = int(input("Please enter a 3-digit number: "))

# Ensure the input is a 3-digit number
if 100 <= number <= 999:
    # Print the number in forward order
    print("Forward order:", number)

    # Calculate the reverse order using modulo and integer division
    hundreds = number // 100
    tens = (number // 10) % 10
    ones = number % 10
    reversed_number = ones * 100 + tens * 10 + hundreds

    # Print the number in reverse order
    print("Reverse order:", reversed_number)
else:
    print("Invalid input. Please enter a 3-digit number.")
