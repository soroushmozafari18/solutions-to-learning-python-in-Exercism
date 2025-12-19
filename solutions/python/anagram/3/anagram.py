def find_anagrams(word, candidates):
    final_list=[]
    for candidate in candidates:
        reference_list=list(word.lower())
        for letter in list(candidate.lower()):
            if letter in reference_list:
                reference_list.remove(letter)
            else:
                reference_list.append('.')
        if reference_list==[] and candidate.lower()!=word.lower():
            final_list.append(candidate)
    return final_list