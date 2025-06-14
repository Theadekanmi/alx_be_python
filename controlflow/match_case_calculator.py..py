def calculate(num1: float, num2: float, operation: str) -> float | str:
    """
    Perform calculation based on the operation using match-case.
    
    Args:
        num1: First number
        num2: Second number
        operation: Mathematical operation (+, -, *, /)
        
    Returns:
        Result of calculation or error message
    """
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Cannot divide by zero."
            return num1 / num2
        case _:
            return "Invalid operation."

def main():
    """Main function to run the calculator program."""
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ").strip()
        
        # Perform calculation
        result = calculate(num1, num2, operation)
        
        # Display result
        if isinstance(result, str):
            print(result)
        else:
            print(f"The result is {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()