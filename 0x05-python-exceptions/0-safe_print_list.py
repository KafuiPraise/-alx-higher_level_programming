#!/bin/python3

def safe_print_list(my_list=[], x=0):
    t = 0

    try:
        for i in my_list:
            if t < x:
                print('{}'.format(my_list[idx]), end='')
                t += 1

        print()
    except TypeError:
        pass
    finally:
        return t
