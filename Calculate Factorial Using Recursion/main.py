def factorial(n):
    # Base condition: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive return: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Test the function
num = 5
print(f"The factorial of {num} is:", factorial(num))