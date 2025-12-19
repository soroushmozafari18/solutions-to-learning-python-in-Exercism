"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return(dish_name, set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return drink_name+' Mocktail'
    else:
        return drink_name+' Cocktail'




def categorize_dish(dish_name, dish_ingredients):
        if dish_ingredients<=VEGAN:
            return dish_name+ ': '+'VEGAN'
        if dish_ingredients<=VEGETARIAN:
            return dish_name+ ': '+'VEGETARIAN'
        if dish_ingredients<=PALEO:
            return dish_name+ ': '+'PALEO'
        if dish_ingredients<=KETO:
            return dish_name+ ': '+'KETO'
        if dish_ingredients<=OMNIVORE:
            return dish_name+ ': '+'OMNIVORE'
def tag_special_ingredients(dish):
    return (dish[0],(set(dish[1]).intersection(SPECIAL_INGREDIENTS)))

def compile_ingredients(dishes):
    lastset=set()
    for dish in dishes:
        lastset= lastset|dish
    return lastset


def separate_appetizers(dishes, appetizers):
    return list(set(dishes)-set(appetizers)) 


def singleton_ingredients(dishes, intersection):
    singletons=set()
    for dish in dishes:
        singletons=singletons|(dish-intersection)
    return singletons
    
        
