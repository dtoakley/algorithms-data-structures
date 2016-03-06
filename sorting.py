
def bubble_sort(a_list):  # O(n^2). Generally regarded as least optimised method.
    for pass_num in range(len(a_list)-1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]

test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(test_list)
print(test_list)


def short_bubble_sort(a_list):  # O(n^2). Improves on bubble sort by stopping short if list is sorted.
    exchanges = True
    pass_num = len(a_list) - 1

    while pass_num and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        pass_num -= 1

test_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(test_list)
print(test_list)


def selection_sort(a_list):  # O(n^2). Same # comparisons as bubble sort, but less exchanges = less processing power.
    for fill_slot in range(len(a_list) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[position_of_max]:
                position_of_max = location

        a_list[fill_slot], a_list[position_of_max] = a_list[position_of_max], a_list[fill_slot]

test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(test_list)
print(test_list)


def insertion_sort(a_list):  # O(n^2). Improves on selection/bubble because shifting takes 1/3 processing as exchanging.
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1

        a_list[position] = current_value

test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(test_list)
print(test_list)


def shell_sort(a_list):  # between O(n) and O(n^2) - depends on increment chosen. Each pass produces a more sorted list.
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        print('After increments of size, ', sublist_count, ' the list is ', a_list)

        sublist_count //= 2


def gap_insertion_sort(a_list, start, gap): # same as insertion sort above but using the gap to select items. The gap
                                                # is the number of slots between each item in the sub list.
    for i in range(start + gap, len(a_list), gap):

        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position-gap] > current_value:
            a_list[position] = a_list[position-gap]
            position -= gap

        a_list[position] = current_value

test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(test_list)
print(test_list)


def merge_sort(a_list):  # O(n log n). However takes up extra space for holding the two halves.
    print('splitting', a_list)

    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_list = a_list[:mid]
        right_list = a_list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                a_list[k] = left_list[i]
                i += 1

            else:
                a_list[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            a_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            a_list[k] = right_list[j]
            j += 1
            k += 1

    print('merging', a_list)

test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(test_list)
print(test_list)


def quick_sort(a_list):  # At best, O(n log n) without the additional memory merge sort needs.
                        # But at worst, if split points are on the edges, it can be O(n^2).
    quick_sort_helper(a_list, 0, len(a_list) - 1)


def quick_sort_helper(a_list, first, last):
    if first < last:

        split_point = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)


def partition(a_list, first, last):
    pivot_value = [a_list[first], len(a_list) // 2, a_list[last]][1]  # the "median of three"

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark += 1

        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]

    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    return right_mark

test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(test_list)
print(test_list)
