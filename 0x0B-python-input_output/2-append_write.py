#!/usr/bin/python3
"""Append to file module."""


def append_write(filename="", text=""):
    """Appends to a file.

    Args:
        filename: name of file to append to.
        text: Text to append.

    Returns:
        Length of text"""

    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))


if __name__ == "__main__":
    append_write()
