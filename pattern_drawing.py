# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print each column in the row
    for col in range(size):
        print("*", end="")  # Print star without a new line
    print()  # After each row, print a newline to move to the next row
    row += 1  # Move to the next row

