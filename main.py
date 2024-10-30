#!/bin/env python
import re

def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results.
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print(" '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print(" {}'{}'".format(prefix, substr))
        print()
    return
def main():
    test_patterns(
        'This is some text -- with punctuation.',
        [
            (r'^\w+', 'word at start of string'),
            (r'\A\w+', 'word at start of string'),
            (r'\w+\S*$', 'word near end of string'),
            (r'\w+\S*\Z', 'word near end of string'),
            (r'\w*t\w*','word containing t'),
            (r'\bt\w+','t at start of word'),
            (r'\w+t\b','t at end of word'),
            (r'\Bt\B','t, not start or end of word'),
        ]
    )
if __name__ == "__main__":
    main()
