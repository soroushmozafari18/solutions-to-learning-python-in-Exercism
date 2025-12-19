def response(hey_bob):
    import string
    if hey_bob.strip().endswith('?') and (not hey_bob.upper()==hey_bob or  set(hey_bob.lower()).isdisjoint(string.ascii_lowercase)):
        return "Sure."
    elif hey_bob.upper()==hey_bob and not hey_bob.endswith('?') and not set(hey_bob.lower()).isdisjoint(string.ascii_lowercase):
        return "Whoa, chill out!" 
    elif hey_bob.upper()==hey_bob and hey_bob.endswith('?') and not set(hey_bob.lower()).isdisjoint(string.ascii_lowercase):
        return "Calm down, I know what I'm doing!"
    elif set(hey_bob)<={'\t',' ','\n','\r'} or hey_bob=='':
        return "Fine. Be that way!"
        
    else:
        return "Whatever."