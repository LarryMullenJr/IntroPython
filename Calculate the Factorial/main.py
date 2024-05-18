# Define a function to calculate the factorial of a number recursively
def factorial(n):
    # Unavoidable answer: factorial of 0 is 1
    if n == 0:
        return 1
    # Run factorial multiplication: multiply n by factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Define the main function
def main():
    try:
        # Ask the user to input a non-negative integer
        num = int(input("Enter a non-negative integer to calculate its factorial: "))
        # Check if the input is negative
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            # Call the factorial function and store the result
            result = factorial(num)
            # Print the result
            print(f"The factorial of {num} is: {result}")


# Check if the script is being run directly and call the main function
if __name__ == "__main__":
    main()
