def is_pangram(sentence):
    reference='abcdefghijklmnopqrstuvwxyz'
    sentence=sentence.lower()
    for i in range(0,26):
        if reference[i] in sentence:
            pass
        else:
            return False
    return True
            
        
    

