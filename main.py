#!/bin/env python
import string

def main():
    t = string.Template('$var')
    print(t.pattern.pattern)

if __name__ == "__main__":
    main()
