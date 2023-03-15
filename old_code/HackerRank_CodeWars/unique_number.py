def find_uniq_1(arr):
    arr.sort()
    return arr[len(arr) - 1] if arr[0] == arr[1] else arr[0]


def find_uniq_2(arr):
    arr.sort()
    if arr[0] != arr[1]:
        return arr[0]
    else:
        return arr[len(arr) - 1]
