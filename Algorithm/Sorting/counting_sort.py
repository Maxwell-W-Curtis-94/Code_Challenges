import timeit
from Algorithm.Sorting.gen_random_list import statis_list


def counting_sort(unsorted_array):
    return unsorted_array


if __name__ == '__main__':
    _unsorted_array = statis_list()
    sorted_array = counting_sort(_unsorted_array.copy())
    print(f"Unsorted {_unsorted_array}, Sorted {sorted_array}")

    t = timeit.Timer(lambda: counting_sort(_unsorted_array.copy()))
    times = 10000
    print(f"Ran {times} times in :{t.timeit(number=times)}")
