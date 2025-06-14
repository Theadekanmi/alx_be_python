def generate_multiplication_table(number: int) -> None:
    """
    Generate and print multiplication table for a given number from 1 to 10.
    
    Args:
        number: The number to generate the table for
    """
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

def main():
    """Main function to get user input and generate table."""
    try:
        number = int(input("Enter a number to see its multiplication table: "))
        generate_multiplication_table(number)
    except ValueError:
        print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    main()