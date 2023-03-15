def countBits(n):
    byt = bin(n)
    byt = str(byt)
    c = 0
    for tok in byt:
        if tok == "1":
            c += 1
    return c
