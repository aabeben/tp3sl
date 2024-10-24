#!/bin/env python
import textwrap
from textwrap_example import sample_text

def main():
    dedented_text = textwrap.dedent(sample_text)
    print('Dedented:')
    print(dedented_text)


if __name__ == "__main__":
    main()
