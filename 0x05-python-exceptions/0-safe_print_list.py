#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_printed = 0
    idx = 0

    while num_printed < x:
        try:
            print(my_list[idx], end='')
            idx += 1
            num_printed += 1
        except IndexError:
            break

    print()
    return num_printed
