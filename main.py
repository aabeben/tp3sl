#!/bin/env python
import re

def main():
    text = 'This some text -- with punctuation.'
    pattern = 'is'

    print('Text: ', text)
    print('Pattern: ', pattern)

    m = re.search(pattern, text)
    print('Search: ', m)
    s = re.fullmatch(pattern, text)
    print('Full match: ', s)

if __name__ == "__main__":
    main()
