def transform(word):
    ay_list=[
'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','bqu','cqu','dqu','fqu','gqu','hqu','jqu','kqu','lqu','mqu','nqu','pqu','qqu','rqu','squ','tqu','vqu','wqu','xqu','yqu','zqu','thr','sch','chqu','stqu','qu','ch','st','th','rh','thr']
    for i in ay_list:
        if word.startswith(i):
            new_word=word[len(i):]+i+'ay'
    if word.startswith(('a','e','i','o','u','xr','yt')):
        new_word=word+'ay'
    return new_word
def translate(text):
     return(' '.join(transform(word) for word in text.split()))
        
    
    