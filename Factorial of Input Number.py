def factorial(n):
    if n < 0:
        raise ValueError("Factorial is defined only for non-negative integers.")
    if not isinstance(n, int):
        raise TypeError("Factorial is defined only for integers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    # Prompt the user to input a positive integer
    n = input("Enter a positive integer: ")
    
    # Try to convert the user's input to an integer
    try:
        n = int(n)
        if n < 0:
            raise ValueError("Factorial is defined only for non-negative integers.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return
    
    # Call the factorial function with the user's input
    result = factorial(n)
    
    # Print the result
    print(f"The factorial of {n} is {result}.")

if __name__ == "__main__":
    main()
