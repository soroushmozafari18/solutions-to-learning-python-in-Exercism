"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return ('un'+word) 


def make_word_groups(vocab_words):
    x=' '.join(vocab_words[1:])
    return (vocab_words[0]+' :: '+vocab_words[0]+x.replace(' ',(' :: '+vocab_words[0])))
    
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    pass


def remove_suffix_ness(word):
    new_word=word[:-4]
    if new_word[-1]=='i':
        return new_word[:-1]+'y'
    else:
        return new_word
    


def adjective_to_verb(sentence, index):
    return (sentence.split()[index]+'en').replace('.','') 