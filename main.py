#!/bin/env python
import textwrap
from textwrap_example import sample_text

def main():
    dedented_text = textwrap.dedent(sample_text).strip()
    print(textwrap.fill(dedented_text, initial_indent='', subsequent_indent=' ' * 4, width=50))

if __name__ == "__main__":
    main()
