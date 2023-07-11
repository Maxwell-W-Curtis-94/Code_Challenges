import timeit
from Algorithm.Sorting.gen_random_list import statis_list


def _partition(unsorted_Array, left, right):
    pivot = unsorted_Array[right]
    pointer = left - 1
    for i in range(left, right):
        if unsorted_Array[i] <= pivot:
            pointer = pointer + 1
            (unsorted_Array[pointer], unsorted_Array[i]) = (unsorted_Array[i], unsorted_Array[pointer])

    (unsorted_Array[pointer+1], unsorted_Array[right]) = (unsorted_Array[right], unsorted_Array[pointer+1])
    return pointer + 1


def quick_sort(unsorted_array, left, right):
    if left < right:
        pivot = _partition(unsorted_array, left, right)
        quick_sort(unsorted_array, left, pivot - 1)
        quick_sort(unsorted_array, pivot + 1, right)
    return unsorted_array


if __name__ == '__main__':
    _unsorted_array = statis_list()
    sorted_array = quick_sort(_unsorted_array.copy(), 0, len(_unsorted_array) - 1)
    print(f"Unsorted {_unsorted_array}\nSorted {sorted_array}")

    t = timeit.Timer(lambda: quick_sort(_unsorted_array.copy(), 0, len(_unsorted_array) - 1))
    times = 10000
    print(f"Ran {times} times in :{t.timeit(number=times)}")
