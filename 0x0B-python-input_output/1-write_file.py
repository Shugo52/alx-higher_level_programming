#!/usr/bin/python3
"""The write module."""


def write_file(filename="", text=""):
    """Writes to a textfile.

    Args:
        filename: File to write to.
        text: string to write to file

    Returns:
        Length of text"""

    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))


if __name__ == "__main__":
    write_file()
