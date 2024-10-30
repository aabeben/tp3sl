#!/bin/env python
import re

def main():
    text = 'This is some text -- with punctuation.'
    pattern = 'is'

    print('Text :', text)
    print('Pattern :', pattern)

    m = re.match(pattern, text)
    print('Match :', m)
    s = re.search(pattern, text)
    print('Search :', s)

if __name__ == "__main__":
    main()
