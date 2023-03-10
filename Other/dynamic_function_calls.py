def sort(array, speed):
    functions = {
        'Bubble': _bubble_sort,
        'Selection': _selection_sort,
        'insertion': _insertion_sort,
    }
    for key in functions:
        print(f'Running {key} Sort: {functions[key](array)}')


def _bubble_sort(array: list):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
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
    pass
