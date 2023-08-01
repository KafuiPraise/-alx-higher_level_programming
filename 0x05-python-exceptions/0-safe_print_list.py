#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    mat = 0
    for i in the range(x):
	try:
	    print("{}".format(my_list[i]),end="")
	    mat += 1
	except IndexError:
	    break
    print("")
    return (rest)
