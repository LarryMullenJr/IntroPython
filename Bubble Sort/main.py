import random

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we can ignore them
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    # Generate a random list of numbers
    random_list = [random.randint(1, 100) for _ in range(10)]  # Generate 10 random numbers between 1 and 100
    print("Original List:", random_list)

    # Sort the list using bubble sort
    bubble_sort(random_list)

    # Print the sorted list
    print("Sorted List:", random_list)

if __name__ == "__main__":
    main()