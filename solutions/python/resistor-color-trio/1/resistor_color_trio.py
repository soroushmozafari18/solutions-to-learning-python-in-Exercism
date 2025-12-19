def label(colors):
    color_list=['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    num_1=color_list.index(colors[0])
    num_2=color_list.index(colors[1])
    num_3=color_list.index(colors[2])
    if num_1==0:
        num_1=''
    number=str(num_1)+str(num_2)+(str(0)*(num_3%3))
    if 3<=num_3<6:
        return number+' kiloohms'
    elif 6<=num_3<9:
        return number+' megaohms'
    elif 9<=num_3<12:
        return number+' gigaohms'
    else:
        return number[:-3]+' kiloohms' if number[-3:]=='000' else number+' ohms'
    
