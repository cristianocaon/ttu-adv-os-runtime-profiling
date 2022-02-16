from quick_sort import quick_sort
from merge_sort import merge_sort


def main():
    arr = [10, 7, 8, 9, 1, 5]
    arr_length = len(arr)
    print_array(arr)

    quick_sort(arr, 0, arr_length - 1)
    print_array(arr, "QuickSort")

    arr = [10, 7, 8, 9, 1, 5]
    merge_sort(arr)
    print_array(arr, "MergeSort")


def print_array(arr, sorting=None):
    if sorting:
        print(f"Sorted array with {sorting}:")
    else:
        print("Current array:")

    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\n")


if __name__ == '__main__':
    main()
