#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max_num = -1
        for i in my_list:
            if i > max_num:
                max_num = i
        return max_num
