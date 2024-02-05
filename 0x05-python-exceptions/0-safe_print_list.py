#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total_success = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            total_success += 1
        except IndexError:
            break
    print()
    return total_success
