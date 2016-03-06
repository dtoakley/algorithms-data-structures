import time

test_list = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]


def binary_search_brute(a_list, item):
    lower_bound = 0
    upper_bound = len(a_list) - 1
    found = False

    while lower_bound <= upper_bound and not found:
        midpoint = (lower_bound + upper_bound) // 2

        if a_list[midpoint] == item:
            found = True

        else:
            if item < a_list[midpoint]:
                upper_bound = midpoint - 1
            else:
                lower_bound = midpoint + 1
    return found

print(binary_search_brute(test_list, 47))


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint+1:], item)

print(binary_search_recursive(test_list, 20))
print(binary_search_recursive(test_list, 47))

