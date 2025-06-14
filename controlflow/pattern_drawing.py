def draw_square_pattern(size: int) -> None:
    """
    Draw a square pattern of asterisks with given size.
    
    Args:
        size: The length of each side of the square
    """
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()  # New line after each row
        row += 1

def main():
    """Main function to get user input and draw the pattern."""
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
        else:
            draw_square_pattern(size)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()