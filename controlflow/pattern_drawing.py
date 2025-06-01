# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Generate square pattern using a while loop
while row < size:
    # Nested for loop to print asterisks in the row
    for _ in range(size):
        print("*", end="")  # Prints without moving to a new line
    print()  # Moves to the next row
    row += 1  # Increments row count
