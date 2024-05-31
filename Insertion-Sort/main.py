import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    # Generate a random list of numbers
    random_list = [random.randint(1, 100) for _ in range(10)]  # Generate 10 random numbers between 1 and 100
    print("Original List:", random_list)

    # Sort the list using insertion sort
    insertion_sort(random_list)

    # Print the sorted list
    print("Sorted List:", random_list)

if __name__ == "__main__":
    main()