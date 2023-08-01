#!/usr/bin/python3
def safe_print_division(a, b):
    t = 0

    try:
        t = a / b
    except ZeroDivisionError:
        t = None
    finally:
        print('Inside result: {}'.format(t))
        return t
