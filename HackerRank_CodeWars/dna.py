def DNA_strand(dna):
    new_dna = ''
    for char in dna:
        if char == 'A':
            new_dna += 'T'
        if char == 'T':
            new_dna += 'A'
        if char == 'C':
            new_dna += 'G'
        if char == 'G':
            new_dna += 'C'
    return new_dna
