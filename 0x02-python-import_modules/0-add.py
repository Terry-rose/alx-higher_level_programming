#!/usr/bin/python3

def main():
    a = 1
    b = 2
    from add_0 import add

    print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    main()

