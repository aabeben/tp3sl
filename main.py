#!/bin/env python
import re

def main():
    text = 'abbaaabbbbaaaaa'
    pattern = 'ab'

    for match in re.findall(pattern, text):
        print('Found {!r}'.format(match))

if __name__ == "__main__":
    main()
