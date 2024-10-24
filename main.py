#!/bin/env python
import textwrap
from textwrap_example import sample_text

def main():
    print(textwrap.fill(sample_text, width=50))


if __name__ == "__main__":
    main()
