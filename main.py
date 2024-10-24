#!/bin/env python
import textwrap
from textwrap_example import sample_text

def main():
    dedented_text = textwrap.dedent(sample_text)
    original = textwrap.fill(dedented_text, width=50)

    print('Original:\n')
    print(original)

    shortened = textwrap.shorten(original, 100)
    shortened_wrapped = textwrap.fill(shortened, width=50)

    print('Shortened:\n')
    print(shortened_wrapped)

if __name__ == "__main__":
    main()
