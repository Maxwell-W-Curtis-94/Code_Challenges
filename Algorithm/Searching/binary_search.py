def iterative_binary_search(search_list, target_value):
    _min, _max = 0, len(search_list) - 1
    steps = 1
    while _min <= _max:
        found_value = (_min + _max) // 2
        if search_list[found_value] == target_value:
            return found_value, f"steps:{steps}"
        elif search_list[found_value] < target_value:
            _min = found_value + 1
        elif search_list[found_value] > target_value:
            _max = found_value - 1
        steps += 1
    return -1, f"steps:{steps}"


def recursive_binary_search():
    pass
