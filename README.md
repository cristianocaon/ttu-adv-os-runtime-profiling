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

To run the program, clone this repository to your local environment: `git clone https://github.com/cristianocaon/aos_project.git`

Change directory to the repository: `cd aos_project`

Run main script: `python3 init.py`
