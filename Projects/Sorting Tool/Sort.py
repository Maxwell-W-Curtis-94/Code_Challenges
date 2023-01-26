"""
pass in an array
this class will choose a sorting algorithm that fits based on the length of the array
and the speed of the sorting needed
"""

import sys
import statistics
import time
import random


def sort(array, speed):
    functions = {
        'Bubble': _bubble_sort,
        'Selection': _selection_sort,
        'Insertion': _insertion_sort,
        'Merge_sort': _merge_sort,
    }
    for key in functions:
        st = time.time()
        print(f'Running {key} Sort: {functions[key](array)}')
        et = time.time()
        print(f'Took: {(et - st) * 1000}ms\n')


def _bubble_sort(array: list):
    if len(array) > 1000:
        raise MemoryError("List is to large for bubble sort")

    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if arr[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


def _selection_sort(array: list):
    for i in range(len(array)):
        min_found = i
        for j in range(i + 1, len(array)):
            if array[min_found] > array[j]:
                min_found = j
        array[i], array[min_found] = array[min_found], array[i]
    return array


def _insertion_sort(array: list):
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def _merge_sort(array: list):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        _merge_sort(left)
        _merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


def _quick_sort():
    pass


def heap_sort():
    pass


def iterative_heapSort():
    pass


def _counting_sort():
    pass


def _radix_sort():
    pass


def _bucket_sort():
    pass


def _gen_list(size):
    large_list = []
    st = time.time()
    for i in range(size):
        large_list.append(random.randint(0, 1000))
    et = time.time()
    print(f"generated list in: {(et - st) * 1000}ms")
    return large_list


if __name__ == '__main__':
    arr = _gen_list(1000)
    sort(array=arr, speed=None)
