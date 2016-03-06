def sequential_search(a_list, item):
    position = 0
    found = False

    while position < len(a_list) and not found:
        if a_list[position] == item:
            found = True
        else:
            position += 1

    return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))


def ordered_sequential_search(a_list, item):
    position = 0
    found = False
    stop = False

    while position < len(a_list) and not found and not stop:
        if a_list[position] == item:
            found = True
        else:
            if a_list[position] > item:
                stop = True
            else:
                position += 1
    return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))
