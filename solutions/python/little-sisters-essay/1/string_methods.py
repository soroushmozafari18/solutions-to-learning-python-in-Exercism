"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    the_list=title.split(' ')
    the_list2=[]
    for word in the_list:
        newword=word.capitalize()
        the_list2.append(newword)
    last_title=' '.join(the_list2)
    return last_title 

def check_sentence_ending(sentence):
   return sentence.endswith('.')

def clean_up_spacing(sentence):
    return sentence.strip()


    
def replace_word_choice(sentence, old_word, new_word):
   return sentence.replace(old_word, new_word)
