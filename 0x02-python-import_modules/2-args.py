#!/usr/bin/python3
from sys import argv

def print_arguments():
    argc = len(argv) - 1  # Subtract 1 to exclude the script name itself

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))

if __name__ == "__main__":
    print_arguments()

