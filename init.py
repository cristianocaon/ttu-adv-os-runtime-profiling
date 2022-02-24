import time
import psutil

from threading import Thread

from util import print_array, print_results
from sorting import quick_sort, merge_sort


def main():

    for iteration in range(1, 4):
        arr = [10, 7, 8, 9, 1, 5]
        arr2 = [10, 7, 8, 9, 1, 5]

        print_array(arr)

        process = psutil.Process()
        start_time = time.time()

        if iteration == 1:
            quick_sort(arr, 0, len(arr) - 1)
            print_array(arr, "QuickSort")
        elif iteration == 2:
            merge_sort(arr)
            print_array(arr, "MergeSort")
        elif iteration == 3:
            quick_sort_thread = Thread(
                target=quick_sort, args=(arr, 0, len(arr) - 1)).start()
            merge_sort_thread = Thread(target=merge_sort, args=(arr2,)).start()
            print_array(arr, "QuickSort")
            print_array(arr2, "MergeSort")

        finish_time = time.time() - start_time
        print_results(finish_time, process)
        print("\n-----------------------//-----------------------")


if __name__ == '__main__':
    main()
