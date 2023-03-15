import timeit
from Algorithm.Sorting.gen_random_list import statis_list


def merge_sort(unsorted_array):
    if len(unsorted_array) > 1:
        mid_point = len(unsorted_array) // 2
        left = unsorted_array[:mid_point]
        right = unsorted_array[mid_point:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
            else:
                unsorted_array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            unsorted_array[k] = right[j]
            j += 1
            k += 1

    return unsorted_array


if __name__ == '__main__':
    _unsorted_array = statis_list()
    sorted_array = merge_sort(_unsorted_array.copy())
    print(f"Unsorted {_unsorted_array}, Sorted {sorted_array}")

    t = timeit.Timer(lambda: merge_sort(_unsorted_array))
    times = 10000
    print(f"Ran {times} times in :{t.timeit(number=times)}")
