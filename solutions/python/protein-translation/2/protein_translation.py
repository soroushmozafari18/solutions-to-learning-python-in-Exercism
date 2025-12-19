def proteins(strand):
    amino_list=[]
    codon_dict={'AUG':'Methionine'
    ,'UUU':'Phenylalanine'
    ,'UUC':'Phenylalanine'
    ,'UUA':'Leucine'
    ,'UUG':'Leucine'
    ,'UCU':'Serine'
    ,'UCC':'Serine'
    ,'UCA':'Serine'
    ,'UCG':'Serine'
    ,'UAU':'Tyrosine'
    ,'UAC':'Tyrosine'
    ,'UGU':'Cysteine'
    ,'UGC':'Cysteine'
    ,'UGG':'Tryptophan'}
    for i in range(0,int(len(strand)/3)):
        codon=strand[3*i:3*i+3]
        if codon in ['UAA','UGA','UAG']:
            return amino_list
        else:
            amino_list.append(codon_dict[codon])
    return amino_list