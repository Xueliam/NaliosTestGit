def mysum(int_list):
    if not int_list:
        return 0
    else:
        return int_list[0] + mysum(int_list[1:])
    


