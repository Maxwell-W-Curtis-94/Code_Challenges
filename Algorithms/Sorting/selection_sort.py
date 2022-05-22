from pprint import pprint

unsorted_list = [
    9, 73, 123, 1, 23, 454, 56, 342, 3, 4, 78, 9
]

for i in range(len(unsorted_list)):
    min_found = i
    for j in range(i + 1, len(unsorted_list)):
        if unsorted_list[min_found] > unsorted_list[j]:
            min_found = j
    unsorted_list[i], unsorted_list[min_found] = unsorted_list[min_found], unsorted_list[i]

pprint(unsorted_list)
