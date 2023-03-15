import timeit
from Algorithm.Sorting.gen_random_list import gen_random_list, statis_list


def selection_sort(unsorted_array):
    for i in range(len(unsorted_array)):
        min_found = i
        for j in range(i + 1, len(unsorted_array)):
            if unsorted_array[min_found] > unsorted_array[j]:
                min_found = j
        unsorted_array[i], unsorted_array[min_found] = unsorted_array[min_found], unsorted_array[i]
    return unsorted_array


if __name__ == '__main__':
    _unsorted_array = statis_list()
    sorted_array = selection_sort(_unsorted_array.copy())
    print(f"Unsorted {_unsorted_array}, Sorted {sorted_array}")

    t = timeit.Timer(lambda: selection_sort(_unsorted_array))
    times = 10000
    print(f"Ran {times} times in :{t.timeit(number=times)}")
