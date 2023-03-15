def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


if __name__ == '__main__':
    array = [9, 4, 5, 2, 4, 5, 1, 3, 6, 7, 3, 4, 5, 2, ]
    print(bubble_sort(arr=array))
