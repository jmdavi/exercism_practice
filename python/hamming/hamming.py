def distance(strand_a, strand_b):
    if type(strand_a) != str or type(strand_a) != str:
        raise ValueError('DNA strands are not strings, wrong type')
    if len(strand_a) != len(strand_b):
        raise ValueError('Length of DNA sequences not equal, Hamming Distance cannot be computed')
    hamming_distance = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hamming_distance += 1
    return hamming_distance
