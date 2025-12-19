def is_pangram(sentence):
    reference='abcdefghijklmnopqrstuvwxyz'
    sentence=sentence.lower()
    for letter in sentence:
        if letter not in reference:
            sentence=sentence.replace(letter,'')
        else:
            pass
    return sorted(set(sentence))==sorted(set(reference))
