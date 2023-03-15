import timeit
from Algorithm.Sorting.gen_random_list import gen_random_list, statis_list


def bubble_sort(array):
    for index in range(len(array)):
        for j in range(0, len(array) - index - 1):
            if array[j] > array[j + 1]:
                hold = array[j]
                array[j] = array[j + 1]
                array[j + 1] = hold

    return array


if __name__ == '__main__':
    unsorted_array = statis_list()
    sorted_array = bubble_sort(unsorted_array.copy())
    print(f"Unsorted {unsorted_array}, Sorted {sorted_array}")

    t = timeit.Timer(lambda: bubble_sort(unsorted_array))
    times = 10000
    print(f"Ran {times} times in :{t.timeit(number=times)}")
