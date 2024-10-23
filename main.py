#!/bin/env python
import string
def main():
    values = {'var': 'foo'}

    t = string.Template("""
                        Variable : $var
                        Escape   : $$
                        Variable in text : ${var}iable
                        """)

    print('TEMPLATE:', t.substitute(values))

    s = """
    Variable : %(var)s
    Escape : %%
    Variable in text: %(var)siable
    """

    print('INTERPOLATION:', s % values)

    s = """
    Variable : {var}
    Escape : {{}}
    Variable in text: {var}iable
    """
    
    print('FORMAT:', s.format(**values))


if __name__ == "__main__":
    main()
