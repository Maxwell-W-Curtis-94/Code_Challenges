positives = filter(lambda x: x > 0, [1, -2, 0, -4, 10])
print(positives)
print(list(positives))

trues = filter(None, [0, 1, False, True, [], [1, 2, 3], '', 'hello'])
print(list(trues))
