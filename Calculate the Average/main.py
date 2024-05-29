def calculate_average(numbers):
    # Get the sum of the list
    total = sum(numbers)
    # Divide the sum by the length of the list
    average = total / len(numbers)
    return average

# Test the function
numbers_list = [10, 20, 30, 40, 50]
average = calculate_average(numbers_list)
print("The average is:", average)