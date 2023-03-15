def count(string):
    alp = {}
    for tok in string:
        if tok not in alp:
            alp[tok] = 1
        else:
            alp[tok] += 1
    return alp
