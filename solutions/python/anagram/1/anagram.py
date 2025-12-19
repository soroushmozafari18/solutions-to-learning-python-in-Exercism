def find_anagrams(word, candidates):
    final_list=[]
    for candidate in candidates:
        if sorted(list(candidate.lower()))==sorted(list(word.lower())) and candidate.lower()!=word.lower():
            final_list.append(candidate)
    return final_list