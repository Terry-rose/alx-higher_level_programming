#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
    - text: a string

    Raises:
    - TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty line
    line = ""

    for char in text:
        # Append the current character to the line
        line += char

        # Check if the current character is one of the specified characters
        if char in ".?:":
            # Print the line with 2 new lines after the specified character
            print(line.strip())
            print()
            # Reset the line for the next iteration
            line = ""

    # Print the remaining part of the text (if any)
    if line:
        print(line.strip())
