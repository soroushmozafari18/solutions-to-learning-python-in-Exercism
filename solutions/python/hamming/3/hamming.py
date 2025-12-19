def distance(strand_a, strand_b):
    if len(strand_b)!=len(strand_a):
        raise ValueError("Strands must be of equal length.")
    return sum(nucleotide_a!=nucleotide_b for nucleotide_a,nucleotide_b in zip(strand_a,strand_b))