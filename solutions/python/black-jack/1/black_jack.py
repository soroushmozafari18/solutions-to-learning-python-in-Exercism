def value_of_card(card):
    if card=='K':
        return 10
    elif card=='Q':
        return 10
    elif card=='J':
        return 10
    elif card=='A':
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):

    if value_of_card(card_one)>value_of_card(card_two):
        return card_one
    if value_of_card(card_one)<value_of_card(card_two):
        return card_two
    if value_of_card(card_one)==value_of_card(card_two):
        return card_one,card_two

def value_ye_card(card):
    if card=='K':
        return 10
    elif card=='Q':
        return 10
    elif card=='J':
        return 10
    elif card=='A':
        return 11
    else:
        return int(card)
def value_of_ace(card_one, card_two):

   if value_ye_card(card_one)+value_ye_card(card_two)<=10:
       return 11
   if value_ye_card(card_one)+value_ye_card(card_two)>10:
       return 1

def is_blackjack(card_one, card_two):
    cards=(value_ye_card(card_one), value_ye_card(card_two))
    return 10 in cards and 11 in cards
        
def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) is value_of_card(card_two)

def can_double_down(card_one, card_two):
    return (value_of_card(card_one)+value_of_card(card_two)) in (9,10,11)