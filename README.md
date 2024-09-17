# CS 5352: Advanced OS Design Project - Spring 2022

## Description: Retrieving, comparing, and presenting process profiling data

The idea of this project is to extract the system vs. user-level information of the running programs and use them to compare the efficiency of two algorithms.

## Requirements

The user-level information should include the running time (from the program starts to when it ends)

The system-level information should include:

1. CPU usage
2. Memory usage
3. Hard drive usage
4. RSS: Resident set size: This is non-swapped physical memory that a process had used
5. VMS: Virtual memory size: This is the total virtual memory used by the process
6. Number of page faults

Running conditions:

1. Algorithm/Program A alone
2. Algorithm/Program B alone
3. Algorithms/Programs A and B concurrent

You present the analysis of your results and findings on comparing the algorithms under different running conditions.

## Instructions

Follow the steps to execute the program:

1. Clone this repository to your local environment: `git clone git@github.com:cristianocaon/ttu-adv-os-runtime-profiling.git`.

2. Change directory to the repository: `cd ttu-adv-os-runtime-profiling`.

3. If applicable, download the dependencies mentioned below.

4. Run main script: `python3 main.py`.

User/system-level information will show up for each of the running conditions:

1. Running QuickSort alone
2. Running MergeSort alone
3. Running both concurrently

## Dependencies

_psutil_: psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. Run `pip install psutil`.

_seaborn_: Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. Run `pip install seaborn`.

_matplotlib_: Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible. Run `pip install matplotlib`.

