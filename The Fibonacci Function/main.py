def fibonacci(n):
    # Base condition: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive return: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
num_terms = 10
print("Fibonacci sequence:")
for i in range(num_terms):
    print(fibonacci(i), end=" ")