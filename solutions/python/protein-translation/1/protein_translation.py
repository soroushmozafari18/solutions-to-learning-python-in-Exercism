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
    while strand!='':
        codon=strand[:3]
        strand= strand[3:]
        if codon in ['UAA','UGA','UAG']:
            return amino_list
        else:
            new_amino=codon_dict.get(codon,'')
            amino_list.append(new_amino)
    return amino_list