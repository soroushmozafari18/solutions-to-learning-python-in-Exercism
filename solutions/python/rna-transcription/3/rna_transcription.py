def to_rna(dna_strand):
    transform_script={'A':'U','T':'A','C':'G','G':'C'}
    return''.join(transform_script[nucleotide]for nucleotide in dna_strand)

    
        
