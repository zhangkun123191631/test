def bubble_sort(nums):
    """
    Sort a sequence with bubble sort in ascending order.
    Returns a new list and does not mutate the input.
    """
    arr = list(nums)
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


bubbleSort = bubble_sort


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("input:", sample)
    print("sorted:", bubble_sort(sample))

    sample2 = [3, -1, 3, 0, -5, 8, 8]
    print("input2:", sample2)
    print("sorted2:", bubble_sort(sample2))
