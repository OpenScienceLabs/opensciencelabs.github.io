"""Clean the output."""

import re
import sys


def remove_ansi_escape_sequences(text: str) -> str:
    """
    Remove ANSI escape sequences from a string.

    Parameters
    ----------
    - text: A string that may contain ANSI escape codes.

    Returns
    -------
    - A string with ANSI escape codes removed.
    """
    # ANSI escape code regex pattern
    ansi_escape_pattern = re.compile(
        r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]"
    )
    return ansi_escape_pattern.sub("", text)


if __name__ == "__main__":
    input_text = sys.stdin.read()
    cleaned_text = remove_ansi_escape_sequences(input_text)
    print(cleaned_text, end="")
