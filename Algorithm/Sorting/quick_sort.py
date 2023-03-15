import timeit
from Algorithm.Sorting.gen_random_list import statis_list


def _partition(unsorted_Array, left, right):
    return 1


def quick_sort(unsorted_array, left, right):
    if right < left:
        pivot = _partition(unsorted_array, left, right)
        quick_sort(unsorted_array, left, pivot - 1)
        quick_sort(unsorted_array, pivot, right)
    return unsorted_array


if __name__ == '__main__':
    _unsorted_array = statis_list()
    sorted_array = quick_sort(_unsorted_array.copy(), 0, len(_unsorted_array) - 1)
    print(f"Unsorted {_unsorted_array}, Sorted {sorted_array}")

    t = timeit.Timer(lambda: quick_sort(_unsorted_array.copy(), 0, len(_unsorted_array) - 1))
    times = 10000
    # print(f"Ran {times} times in :{t.timeit(number=times)}")
