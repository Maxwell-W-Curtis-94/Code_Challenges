import random


def simple_binary_search(arr, target_value):
    # assuming sorted list
    _min, _max = 0, len(arr) - 1
    steps = 1
    while _min <= _max:
        found_value = (_min + _max) // 2
        if arr[found_value] == target_value:
            return found_value, f"steps:{steps}"
        elif arr[found_value] < target_value:
            _min = found_value + 1
        elif arr[found_value] > target_value:
            _max = found_value - 1
        steps += 1
    return -1, f"steps:{steps}"


if __name__ == '__main__':
    sample_array = [random.randint(1, 1000) for i in range(10)]
    sample_array.sort()
    results = simple_binary_search(sample_array, sample_array[5])
    print(results)
