import timeit
from Algorithm.Sorting.gen_random_list import gen_random_list, statis_list


def insertion_sort(unsorted_array):
    for i in range(len(unsorted_array)):
        key = unsorted_array[i]
        j = i - 1
        while j >= 0 and key < unsorted_array[j]:
            unsorted_array[j + 1] = unsorted_array[j]
            j -= 1
        unsorted_array[j + 1] = key
    return unsorted_array


if __name__ == '__main__':
    _unsorted_array = statis_list()
    sorted_array = insertion_sort(_unsorted_array.copy())
    print(f"Unsorted {_unsorted_array}, Sorted {sorted_array}")

    t = timeit.Timer(lambda: insertion_sort(_unsorted_array))
    times = 10000
    print(f"Ran {times} times in :{t.timeit(number=times)}")
