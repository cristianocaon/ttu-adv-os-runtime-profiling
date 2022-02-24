import humanize


def menu():
    print(
        "\nPlease, run the program with one of the options below as argument: \n(E.g. >>> python3 init.py 1)")
    print('''
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    | Select option:              |
    |  1- Run only QuickSort      |
    |  2- Run only MergeSort      |
    |  3- Run both concurrently   |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    ''')
    print("User and system level info will be displayed.\n")


def print_array(arr, sorting=None):
    intro_msg = f"\nSorted array with {sorting}:" if sorting else "\nUnsorted array:"
    print(intro_msg)

    for i in range(len(arr)):
        print(arr[i], end=" ")


def print_results(finish_time, process):
    print("\n\n--- Runtime: %s seconds ---" % finish_time)
    print("--- CPU Usage: %.2f%% ---" %
          process.cpu_percent(finish_time))
    print("--- Memory Usage: %.2f%% ---" %
          process.memory_percent())
    # print("--- Hard Drive Usage: %f%% ---" %
    #       process.disk_usage('/'))
    print("--- RSS: %s ---" %
          humanize.naturalsize(process.memory_info().rss))
    print("--- VMS: %s ---" %
          humanize.naturalsize(process.memory_info().vms))
    print("--- Page Faults: %s ---" %
          process.memory_info().pfaults)
