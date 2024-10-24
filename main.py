#!/bin/env python
import re
import string

class MyTemplate(string.Template):
    delimiter='{{'
    pattern=r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
    '''

def main():
    t = MyTemplate('''
                   {{{{
                   {{var}}
                   ''')
    print('MATCHES:', t.pattern.findall(t.template))
    print('SUBSTITUTE:', t.safe_substitute(var='replacement'))

if __name__ == "__main__":
    main()
