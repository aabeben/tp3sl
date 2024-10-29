#!/bin/env python
import re

def main():
    # Precompile the pattern.
    regexes = [
        re.compile(p)
        for p in ['this', 'that']
    ]
    print(regexes)
    text = 'Does this text match the pattern?'
    print('Text: {!r}\n'.format(text))

    for regex in regexes:
        print('Seeking "{}" ->'.format(regex.pattern), end=' ')

        if regex.search(text):
            print('match')
        else:
            print('no match')

if __name__ == "__main__":
    main()
