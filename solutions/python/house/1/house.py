def versing(verse):
    verse_dic={1:'house that Jack built.',
               2:'malt that lay in',
               3:'rat that ate',
               4:'cat that killed',
               5:'dog that worried',
               6:'cow with the crumpled horn that tossed',
               7:'maiden all forlorn that milked',    
               8:'man all tattered and torn that kissed',
               9:'priest all shaven and shorn that married',
               10:'rooster that crowed in the morn that woke',
               11:'farmer sowing his corn that kept',
               12:'horse and the hound and the horn that belonged to'}
    final_list=[]
    for i in range(verse,0,-1):
        final_list.append(verse_dic[i])
    return 'This is the '+(' the '.join(final_list))    
def recite(start_verse, end_verse):
    recite_list=[]
    for i in range(start_verse,end_verse+1):
        recite_list.append(versing(i))
    return recite_list
    

        

    