def list_division(my_list_1, my_list_2, list_length):
    result = []
    for a in range(list_length):
        try:
            div = my_list_1[a] / my_list_2[a]
            result.append(div)

        except TypeError:
            div = 0
            result.append(div)
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            result.append(div)
            print("division by 0")
        except IndexError:
            div = 0
            result.append(div)
            print("out of range")
        finally:
            pass
    return (result)
