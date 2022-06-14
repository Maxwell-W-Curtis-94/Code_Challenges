def move_zeros(array):
    count = 0
    ar = []
    for tok in array:
        if tok == 0 and tok is not False:
            count += 1
        else:
            ar.append(tok)
    for i in range(count):
        ar.append(0)
    return ar
