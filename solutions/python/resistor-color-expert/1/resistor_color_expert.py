def resistor_label(colors):
    if colors==['black']:
        return '0 ohms'
        pass
    color_list=['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    tol_dict={'grey':0.05,'violet':0.1,'blue':0.25,'green':0.5,'brown':1,'red':2,'gold':5,'silver':10}
    number=''    #making the main number
    for color in colors[:-2]:
        number=number+str(color_list.index(color))
    multiplier=color_list.index(colors[-2])
    number+=multiplier*'0'      #determining the zeros and metric
    number=int(number)
    counter=0
    while number>=1000:
        number=number/1000
        counter+=1
    prefix=['','kilo','mega','giga'][counter]
    tolerance=tol_dict[colors[-1]]           #determinig the tolerance
    return f'{number:g} {prefix}ohms ±{tolerance}%'