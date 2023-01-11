#!/usr/bin/python3
"""Read File Module."""


def read_file(filename=""):
    """Prints a textfile to stdout.

    Args:
        filename: File to read contents.

    Returns:
        Number of characters read from <filename>."""

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")


if __name__ == "__main__":
    read_file()
