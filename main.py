#!/bin/env python
import string

values = {'var': 'foo'}
t = string.Template("$var is here but $missing is not provided")
def main():
    try:
        print('substitute()       :', t.substitute(values))
    except KeyError as err:
        print('ERROR:', str(err))
print('safe_substitute():', t.safe_substitute(values))
if __name__ == "__main__":
    main()
