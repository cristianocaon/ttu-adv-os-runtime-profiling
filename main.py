import os
import time
import random
import psutil
import shutil
import tracemalloc

from multiprocessing import Process

from util import print_results, display_results
from sorting import quick_sort, merge_sort


def main():
    array_size = int(input("Please, enter the size of the array: "))

    if array_size < 1:
        print("Array size must be greater than 1!")
        return

    data = {
        "runtime": [],
        "cpu_usage": [],
        "memory_usage": [],
        "hard_drive_usage": [],
        "rss": [],
        "vms": [],
        "page_faults": []
    }

    labels = ['QuickSort', 'MergeSort', 'Concurrent']

    for iteration in range(0, 3):
        arr = []
        arr2 = []
        for i in range(0, array_size):
            n = random.randint(0, array_size)
            arr.append(n)
            arr2.append(n)

        process = psutil.Process()
        tracemalloc.start()
        start_time = time.time()

        if iteration == 0:
            print("\n--------- QuickSort ---------")
            quick_sort(arr, 0, len(arr) - 1)
        elif iteration == 1:
            print("\n--------- MergeSort ---------")
            merge_sort(arr)
        elif iteration == 2:
            print("\n--------- Concurrent ---------")
            quick_sort_proc = Process(
                target=quick_sort, args=(arr, 0, len(arr) - 1))
            merge_sort_proc = Process(target=merge_sort, args=(arr2,))
            quick_sort_proc.start()
            merge_sort_proc.start()
            quick_sort_proc.join()
            merge_sort_proc.join()

        finish_time = time.time() - start_time
        memory_usage = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        disk_usage = shutil.disk_usage(os.getcwd())
        process.cpu_percent(interval=None)

        data["runtime"].append(finish_time)
        data["cpu_usage"].append(process.cpu_percent(interval=None) / psutil.cpu_count() * 100)
        data["memory_usage"].append(memory_usage[0] // 1000)
        data["hard_drive_usage"].append(disk_usage[1] // 2 ** 30)
        data["rss"].append(process.memory_info().rss // 2 ** 20)
        data["vms"].append(process.memory_info().vms // 2 ** 30)
        data["page_faults"].append(process.memory_info().pfaults // 1000)

        print_results(data, iteration)

    display_results(data, labels)


if __name__ == '__main__':
    main()
