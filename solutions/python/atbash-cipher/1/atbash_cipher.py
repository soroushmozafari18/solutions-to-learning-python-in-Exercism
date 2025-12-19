def encode(plain_text):
    import string
    cipher_dict=dict()
    for i in range(0,26):
        cipher_dict[string.ascii_lowercase[i]]=string.ascii_lowercase[25-i]
    mytranslator=str.maketrans(cipher_dict)
    plain_text=((plain_text.lower()).translate(mytranslator)).replace(' ','')
    for letter in plain_text:
        if letter in '.,':
            plain_text=plain_text.replace(letter,'')
    mynewstring=''
    for i in range(0,len(plain_text)):
        mynewstring+=plain_text[i]
        if (i+1)%5==0 and (i+1)!=len(plain_text):
            mynewstring+=' '
    return mynewstring
def decode(ciphered_text):
    import string
    cipher_dict=dict()
    for i in range(0,26):
        cipher_dict[string.ascii_lowercase[25-i]]=string.ascii_lowercase[i]
    mytranslator=str.maketrans(cipher_dict)
    ciphered_text=((ciphered_text.lower()).translate(mytranslator)).replace(' ','')
    for letter in ciphered_text:
        if letter in '.,':
            ciphered_text=ciphered_text.replace(letter,'')
    return ciphered_text