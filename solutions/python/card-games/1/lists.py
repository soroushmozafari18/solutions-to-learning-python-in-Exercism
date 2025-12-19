"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
  return [number,number+1,number+2]


def concatenate_rounds(rounds_1, rounds_2):
   return rounds_1+rounds_2

def list_contains_round(rounds, number):
    return number in rounds

    
def card_average(hand):
    return sum(hand)/len(hand)

def approx_average_is_average(hand):
    approx_average1= (hand[0]+hand[-1])/2
    approx_average2= float(hand[int((len(hand)-1)/2)])
    average=sum(hand)/len(hand)
    return((approx_average1==average)or (approx_average2==average))

def average_even_is_average_odd(hand):
    even_list=[]
    odd_list=[]
    for i in range(0,len(hand)):
        if not i%2:
            odd_list.append(hand[i])
        else:
            even_list.append(hand[i])
    average_even= sum(even_list)/len(even_list)
    average_odd= sum(odd_list)/len(odd_list)
    return(average_even==average_odd)
         
def maybe_double_last(hand):
    if hand[-1]==11:
        del hand[-1]
        hand.append(22)
    return hand
    