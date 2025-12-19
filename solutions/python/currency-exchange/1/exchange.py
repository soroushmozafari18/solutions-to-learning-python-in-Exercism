def exchange_money(budget, exchange_rate):
    exchanged_money=budget/exchange_rate
    return exchanged_money


def get_change(budget, exchanging_value):
    left_money=budget-exchanging_value
    return left_money

def get_value_of_bills(denomination, number_of_bills):
    value_of_bills=denomination*number_of_bills
    return value_of_bills

def get_number_of_bills(budget, denomination):
    number_of_bills=budget//denomination   
    return number_of_bills           
    
def get_leftover_of_bills(budget, denomination):
    leftover_of_bills=budget%denomination
    return leftover_of_bills

def exchangeable_value(budget, exchange_rate, spread, denomination):
    actual_exchange_rate= ((spread/100)+1)*exchange_rate
    exchanged_money=budget/actual_exchange_rate
    exchangeable_value=exchanged_money-(exchanged_money%denomination)
    return exchangeable_value
    