#!/usr/bin/python3

def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        return str[:n] + str[n + 1:]
    else:
        return str

if __name__ == "__main__":
    remove_char_at("Best School", 3)
    remove_char_at("Chicago", 2)
    remove_char_at("C is fun!", 0)
    remove_char_at("School", 10)
    remove_char_at("Python", -2)
