#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Usage:
    $ ./101-generator.py | ./101-stats.py

Author:
    Your Name

Date:
    February 7, 2024
"""

import sys

def print_metrics(total_size, status_counts):
    """
    Prints the computed metrics.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing status code counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))

if __name__ == "__main__":
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            try:
                parts = line.split()
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size

                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1

                if i % 10 == 0:
                    print_metrics(total_size, status_counts)
            except ValueError:
                pass  # Ignore lines with incorrect format
    except KeyboardInterrupt:
        pass

    print_metrics(total_size, status_counts)

