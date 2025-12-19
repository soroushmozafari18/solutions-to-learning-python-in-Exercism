def to_rna(dna_strand):
    RNA_list=[]
    for nucleotide in dna_strand:
        if nucleotide=='G':
            RNA_list.append('C')
        if nucleotide=='C':
            RNA_list.append('G')
        if nucleotide=='A':
            RNA_list.append('U')
        if nucleotide=='T':
            RNA_list.append('A')
        else:
            pass
    return(''.join(RNA_list))
        
