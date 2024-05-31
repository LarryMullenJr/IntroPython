import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    # Generate a random list of numbers
    random_list = [random.randint(1, 100) for _ in range(10)]  # Generate 10 random numbers between 1 and 100
    print("Original List:", random_list)

    # Sort the list using merge sort
    merge_sort(random_list)

    # Print the sorted list
    print("Sorted List:", random_list)

if __name__ == "__main__":
    main()