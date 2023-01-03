#!/usr/bin/python3
"""The 5-text_indentation module."""


def text_indentation(text):
    """Inserts 2 new lines after 3 select characters and prints to stdout

    Args:
        text (str): Text to parse and insert newlines.

    Returns:
        None.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Strip spaces around initial text
    text = text.strip(" ")

    # Strip spaces around each printed line of text on stdout
    text = text.split("\n")
    text = [_text.strip(" ") for _text in text]
    text = "\n".join(text)

    # Create tokens and token dict for easy substitution
    tokens = ".?:"
    token_dict = {token: f"{token}\n\n" for token in tokens}

    # Replace token occurences in text with dict values
    for token in tokens:
        text = text.split(token)
        text = [_text.lstrip(" ") for _text in text]
        text = token.join(text)
        text = text.replace(token, token_dict[token])

    print(text, end="")
