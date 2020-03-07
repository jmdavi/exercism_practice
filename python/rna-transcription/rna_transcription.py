def to_rna(dna_strand):
    #replace with temporary placeholder to avoid problems with same letters
    dna_transformed = dna_strand.replace('G','1')\
        .replace('C','2')\
        .replace('T','3')\
        .replace('A','4')
    return dna_transformed\
        .replace('1','C')\
        .replace('2','G')\
        .replace('3','A')\
        .replace('4','U')
    pass
