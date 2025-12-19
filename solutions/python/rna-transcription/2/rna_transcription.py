def to_rna(dna_strand):
    transform_script={'A':'U','T':'A','C':'G','G':'C'}
    RNA_list=[]
    for nucleotide in dna_strand:
        RNA_list.append(transform_script[nucleotide])
    return(''.join(RNA_list))
        
