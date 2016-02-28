import time


def binary_search_brute_force(list, target):
    lower_bound = 0
    upper_bound = len(list)

    while True:
        if lower_bound == upper_bound:
            return -1

        middle_index = (lower_bound + upper_bound) // 2
        middle_item = list[middle_index]

        if target == middle_item:
            return middle_index
        elif target > middle_item:
            lower_bound = middle_index + 1
        elif target < middle_item:
            upper_bound = middle_index


def binary_search_recursion(list, target, lower_bound=0, upper_bound=None):

    upper_bound = len(list) if upper_bound is None else upper_bound

    if lower_bound == upper_bound:
        return -1

    middle_index = (lower_bound + upper_bound) // 2
    middle_item = list[middle_index]

    if target == middle_item:
        return middle_index
    elif target > middle_item:
        return binary_search_recursion(list, target, middle_index + 1, upper_bound)
    elif target < middle_item:
        return binary_search_recursion(list, target, lower_bound, middle_index)

test_list = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]

assert (binary_search_recursion(test_list, 20) == -1)
assert (binary_search_recursion(test_list, 99) == -1)
assert(binary_search_recursion(test_list, 1) == -1)

print(binary_search_recursion(test_list, 47))

for (i, v) in enumerate(test_list):
    assert (binary_search_recursion(test_list, v) == i)


t0 = time.clock()

t1 = time.clock()