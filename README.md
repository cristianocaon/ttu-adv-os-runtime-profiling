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

1. Clone this repository to your local environment: `git clone https://github.com/cristianocaon/AOS_project.caon.git`

2. Change directory to the repository: `cd aos_project`.

3. If applicable, download the dependencies mentioned below.

4. Run main script: `python3 init.py`.

User/system-level information will show up for each of the running conditions:

1. Running QuickSort alone
2. Running MergeSort alone
3. Running both concurrently

## Dependencies

_psutil_: psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. Run `pip install psutil`.

_humanize_: This modest package contains various common humanization utilities, like turning a number into a fuzzy human-readable duration ("3 minutes ago") or into a human-readable size or throughput. Run `pip install humanize`.
