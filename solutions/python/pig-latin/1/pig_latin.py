def transform(word):
    if word.startswith(('a','e','i','o','u','xr','yt')):
        newtext=word+'ay'
    elif word.startswith(('bqu','cqu','dqu','fqu','gqu','hqu','jqu','kqu','lqu','mqu','nqu','pqu','qqu','rqu','squ','tqu','vqu','wqu','xqu','yqu','zqu','thr','sch')):
        newtext=word[3:]+word[:3]+'ay'
    elif word.startswith(('chqu','stqu')):
        newtext=word[4:]+word[:4]+'ay'
    elif word.startswith('qu'):
        newtext=word[2:]+word[:2]+'ay'
    elif word.startswith(('ch','st','th','rh')):
        newtext=word[2:]+word[:2]+'ay'
    elif word.startswith(('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')):
        newtext=word[1:]+word[0]+'ay'
    return newtext
def translate(text):
     return(' '.join(transform(word) for word in text.split()))
        
    
    