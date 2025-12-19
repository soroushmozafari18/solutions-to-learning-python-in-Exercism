def is_pangram(sentence):
    reference='abcdefghijklmnopqrstuvwxyz'
    sentence=sentence.lower()
    for letter in reference:
        if letter in sentence:
            pass
        else:
            return False
    return True
            
    

