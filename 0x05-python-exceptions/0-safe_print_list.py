#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list_len = sum(1 for item in my_list)
    new = [my_list[i] for i in range(list_len) if i < x and i <= list_len]
    try:
        print(*new, sep='')
    except:
        pass
    return sum(1 for item in new)
