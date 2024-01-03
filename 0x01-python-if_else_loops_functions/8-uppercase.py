#!/usr/bin/python3

def uppercase(s):
    for c in s:
        print("{}".format(chr(ord(c) - 32) if ord('a') <= ord(c) <= ord('z') else c), end="")
    print()

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
