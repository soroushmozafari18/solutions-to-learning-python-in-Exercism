def commands(binary_str):
    orders=(['','wink'],['','double blink'],['','close your eyes'],['','jump'])
    orders_list=[]
    for i in range(1,5):
        orders_list.append(orders[i-1][int(binary_str[5-i])])
    while '' in orders_list:
        orders_list.remove('')
    if binary_str[0]=='1' :
        orders_list.reverse()
    return orders_list
