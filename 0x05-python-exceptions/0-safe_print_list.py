def safe_print_list(my_list=[], x=0):
    limit = 0
    for a in my_list:
        try:
            if limit < x:
                print(a, end='')
                limit += 1
        except:
            break
    print()
    return limit
